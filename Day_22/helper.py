RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


class Tile:
    def __init__(self, num, data, row_offset, col_offset, above=None, below=None, left=None, right=None):
        self.num = num
        self.row_offset = row_offset + 1    # Rows are indexed starting at 1
        self.col_offset = col_offset + 1    # Columns are indexed starting at 1
        self.data = data
        self.above = above
        self.below = below
        self.left = left
        self.right = right


class Map:
    def __init__(self, curr_tile, tile_size, curr_row=0, curr_col=0, direction=RIGHT):
        self.curr_tile = curr_tile
        self.tile_size = tile_size
        self.curr_row = curr_row
        self.curr_col = curr_col
        self.direction = direction

    def move_up(self):
        if self.curr_row > 0:
            next_direction = UP
            next_col = self.curr_col
            next_row = self.curr_row - 1
            next_tile = self.curr_tile
        else:
            next_tile = self.curr_tile.above
            if next_tile.below == self.curr_tile:
                next_direction = UP
                next_col = self.curr_col
                next_row = self.tile_size - 1
            elif next_tile.left == self.curr_tile:
                next_direction = RIGHT
                next_col = 0
                next_row = self.curr_col
            elif next_tile.above == self.curr_tile:
                next_direction = DOWN
                next_col = self.tile_size - self.curr_col - 1
                next_row = 0
            else:
                next_direction = LEFT
                next_col = self.tile_size - 1
                next_row = self.tile_size - self.curr_col - 1

        if next_tile.data[next_row][next_col] == '.':
            self.curr_tile = next_tile
            self.direction = next_direction
            self.curr_col = next_col
            self.curr_row = next_row

    def move_down(self):
        if self.curr_row < self.tile_size - 1:
            next_direction = DOWN
            next_col = self.curr_col
            next_row = self.curr_row + 1
            next_tile = self.curr_tile
        else:
            next_tile = self.curr_tile.below
            if next_tile.above == self.curr_tile:
                next_direction = DOWN
                next_col = self.curr_col
                next_row = 0
            elif next_tile.right == self.curr_tile:
                next_direction = LEFT
                next_col = self.tile_size - 1
                next_row = self.curr_col
            elif next_tile.below == self.curr_tile:
                next_direction = UP
                next_col = self.tile_size - self.curr_col - 1
                next_row = self.tile_size - 1
            else:
                next_direction = RIGHT
                next_col = 0
                next_row = self.tile_size - self.curr_col - 1

        if next_tile.data[next_row][next_col] == '.':
            self.curr_tile = next_tile
            self.direction = next_direction
            self.curr_col = next_col
            self.curr_row = next_row

    def move_left(self):
        if self.curr_col > 0:
            next_direction = LEFT
            next_col = self.curr_col - 1
            next_row = self.curr_row
            next_tile = self.curr_tile
        else:
            next_tile = self.curr_tile.left
            if next_tile.right == self.curr_tile:
                next_direction = LEFT
                next_col = self.tile_size - 1
                next_row = self.curr_row
            elif next_tile.below == self.curr_tile:
                next_direction = UP
                next_col = self.tile_size - self.curr_row - 1
                next_row = self.tile_size - 1
            elif next_tile.left == self.curr_tile:
                next_direction = RIGHT
                next_col = 0
                next_row = self.tile_size - self.curr_row - 1
            else:
                next_direction = DOWN
                next_col = self.curr_row
                next_row = 0

        if next_tile.data[next_row][next_col] == '.':
            self.curr_tile = next_tile
            self.direction = next_direction
            self.curr_col = next_col
            self.curr_row = next_row

    def move_right(self):
        if self.curr_col < self.tile_size - 1:
            next_direction = RIGHT
            next_col = self.curr_col + 1
            next_row = self.curr_row
            next_tile = self.curr_tile
        else:
            next_tile = self.curr_tile.right
            if next_tile.left == self.curr_tile:
                next_direction = RIGHT
                next_col = 0
                next_row = self.curr_row
            elif next_tile.above == self.curr_tile:
                next_direction = DOWN
                next_col = self.tile_size - self.curr_row - 1
                next_row = 0
            elif next_tile.right == self.curr_tile:
                next_direction = LEFT
                next_col = self.tile_size - 1
                next_row = self.tile_size - self.curr_row - 1
            else:
                next_direction = UP
                next_col = self.curr_row
                next_row = self.tile_size - 1

        if next_tile.data[next_row][next_col] == '.':
            self.curr_tile = next_tile
            self.direction = next_direction
            self.curr_col = next_col
            self.curr_row = next_row

    def follow_instructions(self, instructions):
        instructions = instructions.replace('R', ',R,')
        instructions = instructions.replace('L', ',L,')
        instructions = instructions.strip().split(',')

        for instruction in instructions:
            if instruction == 'L':
                if self.direction == UP:
                    self.direction = LEFT
                elif self.direction == DOWN:
                    self.direction = RIGHT
                elif self.direction == LEFT:
                    self.direction = DOWN
                else:
                    self.direction = UP
            elif instruction == 'R':
                if self.direction == UP:
                    self.direction = RIGHT
                elif self.direction == DOWN:
                    self.direction = LEFT
                elif self.direction == LEFT:
                    self.direction = UP
                else:
                    self.direction = DOWN
            else:
                steps = int(instruction)
                for _ in range(steps):
                    if self.direction == UP:
                        self.move_up()
                    elif self.direction == DOWN:
                        self.move_down()
                    elif self.direction == LEFT:
                        self.move_left()
                    else:
                        self.move_right()
