AIR = 0
ROCK = 1
SAND = 2


class Cave:
    def __init__(self, filename, floor):
        self.min_x = 500
        self.max_x = 500
        self.max_y = 0
        self.rock_pts = []

        with open(filename) as file:
            for line in file:
                coordinates = line.strip().split(" -> ")
                curr_pts = []
                for coordinate in coordinates:
                    [x, y] = coordinate.split(",")
                    if len(curr_pts) == 0:
                        curr_pts.append((x, y))
                    elif len(curr_pts) == 1:
                        curr_pts.append((x, y))
                        self._calc_line(curr_pts)
                    else:
                        curr_pts.pop(0)
                        curr_pts.append((x, y))
                        self._calc_line(curr_pts)

        if floor:
            width = self.max_x - self.min_x
            self._calc_line([[self.min_x-width*3, self.max_y+2], [self.max_x+width*3, self.max_y+2]])

        self.structure = [[AIR for _ in range(self.max_x-self.min_x+1)] for _ in range(self.max_y+1)]

        for pt in self.rock_pts:
            self.structure[pt[1]][pt[0]-self.min_x] = ROCK

    def _calc_line(self, pts):
        (x1, y1) = (int(pts[0][0]), int(pts[0][1]))
        (x2, y2) = (int(pts[1][0]), int(pts[1][1]))

        self.min_x = min(self.min_x, x1, x2)
        self.max_x = max(self.max_x, x1, x2)
        self.max_y = max(self.max_y, y1, y2)

        if y1 < y2:
            for i in range(y1, y2 + 1):
                self.rock_pts.append([x1, i])
        elif y2 < y1:
            for i in range(y2, y1 + 1):
                self.rock_pts.append([x1, i])
        elif x1 < x2:
            for i in range(x1, x2 + 1):
                self.rock_pts.append([i, y1])
        else:
            for i in range(x2, x1 + 1):
                self.rock_pts.append([i, y1])

    def __repr__(self):
        text = ""
        for row in self.structure:
            for elem in row:
                if elem == AIR:
                    text += '.'
                elif elem == ROCK:
                    text += '#'
                else:
                    text += 'o'
            text += '\n'

        return text

    def sim_sand_grain(self):
        sand_x = 500
        sand_y = 0

        if self.structure[sand_y][sand_x-self.min_x] == SAND:
            # Filled to the top
            return False

        while True:
            if sand_x-1 < self.min_x or sand_y+1 > self.max_y or sand_x + 1 > self.max_x:
                # Out of bounds
                return False

            below_left_filled = self.structure[sand_y+1][sand_x-1-self.min_x] != AIR
            below_filled = self.structure[sand_y+1][sand_x-self.min_x] != AIR
            below_right_filled = self.structure[sand_y+1][sand_x+1-self.min_x] != AIR

            if below_left_filled and below_filled and below_right_filled:
                # Sand settled at a position
                self.structure[sand_y][sand_x-self.min_x] = SAND
                return True

            if not below_filled:
                sand_y += 1
            elif not below_left_filled:
                sand_y += 1
                sand_x -= 1
            elif not below_right_filled:
                sand_y += 1
                sand_x += 1


# Part 1
cave = Cave("input.txt", floor=False)
num_grains = 0
while cave.sim_sand_grain():
    num_grains += 1
print(num_grains)

# Part 2
cave = Cave("input.txt", floor=True)
num_grains = 0
while cave.sim_sand_grain():
    num_grains += 1
print(num_grains)

