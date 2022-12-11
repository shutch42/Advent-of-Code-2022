import os

class End:
    def __init__(self):
        self.x = 0
        self.y = 0


class Rope:
    def __init__(self, length):
        self.links = []
        for i in range(length):
            self.links.append(End())
        self.tail_positions = [(0, 0)]

    def touching(self, num):
        head = self.links[num-1]
        tail = self.links[num]
        if head.x - 1 <= tail.x <= head.x + 1 and head.y - 1 <= tail.y <= head.y + 1:
            return True
        else:
            return False

    def move_chain(self, num):
        head = self.links[num-1]
        tail = self.links[num]
        if not self.touching(num):
            if head.x == tail.x:
                # head and tail aligned horizontally
                if head.y > tail.y:
                    tail.y += 1
                else:
                    tail.y -= 1
            elif head.y == tail.y:
                # head and tail aligned vertically
                if head.x > tail.x:
                    tail.x += 1
                else:
                    tail.x -= 1
            elif head.x > tail.x and head.y > tail.y:
                # head NE of tail
                tail.x += 1
                tail.y += 1
            elif head.x > tail.x and head.y < tail.y:
                # head SE of tail
                tail.x += 1
                tail.y -= 1
            elif head.x < tail.x and head.y > tail.y:
                # head NW of tail
                tail.x -= 1
                tail.y += 1
            else:
                # head SW of tail
                tail.x -= 1
                tail.y -= 1

    def check_coordinates(self):
        last_elem = len(self.links) - 1
        coordinates = (self.links[last_elem].x, self.links[last_elem].y)
        if coordinates not in self.tail_positions:
            self.tail_positions.append(coordinates)

    def move_right(self):
        self.links[0].x += 1
        for i in range(1, len(self.links)):
            self.move_chain(i)
        self.check_coordinates()

    def move_left(self):
        self.links[0].x -= 1
        for i in range(1, len(self.links)):
            self.move_chain(i)
        self.check_coordinates()

    def move_up(self):
        self.links[0].y += 1
        for i in range(1, len(self.links)):
            self.move_chain(i)
        self.check_coordinates()

    def move_down(self):
        self.links[0].y -= 1
        for i in range(1, len(self.links)):
            self.move_chain(i)
        self.check_coordinates()

    def print(self):
        os.system('clear')
        terminal = [""] * 24
        terminal[23] = "Move rope with WASD or arrow keys"
        for link in self.links:
            row = 22 - link.y
            column = link.x
            terminal_str = terminal[row]
            for i in range(column):
                if i >= len(terminal_str):
                    terminal_str += " "
            if column == len(terminal_str):
                terminal_str += "X"
            else:
                terminal_str = terminal_str[:column] + 'X' + terminal_str[column+1:]
            terminal[row] = terminal_str

        for line in terminal:
            print(line)
