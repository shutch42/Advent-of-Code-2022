from helper import *

#################################################
# Hard-coded input for each file is stored here #
#################################################


def load_example_pt1():
    tile_size = 4
    with open("example_input.txt") as file:
        lines = file.readlines()
        tile_1 = Tile(1, [line.strip() for line in lines[:tile_size]], 0, 2 * tile_size)
        tile_2 = Tile(2, [line.strip()[:tile_size] for line in lines[tile_size:2 * tile_size]], tile_size, 0)
        tile_3 = Tile(3, [line.strip()[tile_size:2 * tile_size] for line in lines[tile_size:2 * tile_size]], tile_size,
                      tile_size)
        tile_4 = Tile(4, [line.strip()[tile_size * 2:tile_size * 3] for line in lines[tile_size:2 * tile_size]], tile_size,
                      2 * tile_size)
        tile_5 = Tile(5, [line.strip()[:tile_size] for line in lines[tile_size * 2:tile_size * 3]], 2 * tile_size,
                      2 * tile_size)
        tile_6 = Tile(6, [line.strip()[tile_size:tile_size * 2] for line in lines[tile_size * 2:tile_size * 3]],
                      2 * tile_size, 3 * tile_size)
        instructions = lines[tile_size * 3 + 1]

    curr_tile = tile_1
    tile_1.above = tile_5
    tile_1.left = tile_1
    tile_1.right = tile_1
    tile_1.below = tile_4

    tile_2.left = tile_4
    tile_2.right = tile_3
    tile_2.above = tile_2
    tile_2.below = tile_2

    tile_3.left = tile_2
    tile_3.right = tile_4
    tile_3.above = tile_3
    tile_3.below = tile_3

    tile_4.left = tile_3
    tile_4.right = tile_2
    tile_4.above = tile_1
    tile_4.below = tile_5

    tile_5.above = tile_4
    tile_5.below = tile_1
    tile_5.left = tile_6
    tile_5.right = tile_6

    tile_6.left = tile_5
    tile_6.right = tile_5
    tile_6.above = tile_6
    tile_6.below = tile_6

    return Map(curr_tile, tile_size), instructions


def load_input_pt1():
    tile_size = 50
    with open("input.txt") as file:
        lines = file.readlines()
        tile_1 = Tile(1, [line.strip()[:tile_size] for line in lines[:tile_size]], 0, tile_size)
        tile_2 = Tile(2, [line.strip()[tile_size:2*tile_size] for line in lines[:tile_size]], 0, 2*tile_size)
        tile_3 = Tile(3, [line.strip()[:tile_size] for line in lines[tile_size:2*tile_size]], tile_size, tile_size)
        tile_4 = Tile(4, [line.strip()[:tile_size] for line in lines[tile_size*2:tile_size*3]], 2*tile_size, 0)
        tile_5 = Tile(5, [line.strip()[tile_size:2*tile_size] for line in lines[tile_size*2:tile_size*3]], 2*tile_size, tile_size)
        tile_6 = Tile(6, [line.strip()[:tile_size] for line in lines[tile_size*3:tile_size*4]], 3*tile_size, 0)
        instructions = lines[tile_size*4+1]

    curr_tile = tile_1
    tile_1.above = tile_5
    tile_1.left = tile_2
    tile_1.right = tile_2
    tile_1.below = tile_3

    tile_2.left = tile_1
    tile_2.right = tile_1
    tile_2.above = tile_2
    tile_2.below = tile_2

    tile_3.above = tile_1
    tile_3.below = tile_5
    tile_3.left = tile_3
    tile_3.right = tile_3

    tile_4.above = tile_6
    tile_4.left = tile_5
    tile_4.right = tile_5
    tile_4.below = tile_6

    tile_5.above = tile_3
    tile_5.below = tile_1
    tile_5.left = tile_4
    tile_5.right = tile_4

    tile_6.left = tile_6
    tile_6.right = tile_6
    tile_6.above = tile_4
    tile_6.below = tile_4

    return Map(curr_tile, tile_size), instructions


def load_example_pt2():
    tile_size = 4
    with open("example_input.txt") as file:
        lines = file.readlines()
        tile_1 = Tile(1, [line.strip() for line in lines[:tile_size]], 0, 2 * tile_size)
        tile_2 = Tile(2, [line.strip()[:tile_size] for line in lines[tile_size:2 * tile_size]], tile_size, 0)
        tile_3 = Tile(3, [line.strip()[tile_size:2 * tile_size] for line in lines[tile_size:2 * tile_size]], tile_size,
                      tile_size)
        tile_4 = Tile(4, [line.strip()[tile_size * 2:tile_size * 3] for line in lines[tile_size:2 * tile_size]], tile_size,
                      2 * tile_size)
        tile_5 = Tile(5, [line.strip()[:tile_size] for line in lines[tile_size * 2:tile_size * 3]], 2 * tile_size,
                      2 * tile_size)
        tile_6 = Tile(6, [line.strip()[tile_size:tile_size * 2] for line in lines[tile_size * 2:tile_size * 3]],
                      2 * tile_size, 3 * tile_size)
        instructions = lines[tile_size * 3 + 1]

    curr_tile = tile_1
    tile_1.above = tile_2
    tile_1.left = tile_3
    tile_1.right = tile_6
    tile_1.below = tile_4

    tile_2.above = tile_1
    tile_2.left = tile_6
    tile_2.right = tile_3
    tile_2.below = tile_5

    tile_3.above = tile_1
    tile_3.below = tile_5
    tile_3.left = tile_2
    tile_3.right = tile_4

    tile_4.above = tile_1
    tile_4.left = tile_3
    tile_4.right = tile_6
    tile_4.below = tile_5

    tile_5.above = tile_4
    tile_5.left = tile_3
    tile_5.right = tile_6
    tile_5.below = tile_2

    tile_6.above = tile_4
    tile_6.left = tile_5
    tile_6.right = tile_1
    tile_6.below = tile_2

    return Map(curr_tile, tile_size), instructions


def load_input_pt2():
    tile_size = 50
    with open("input.txt") as file:
        lines = file.readlines()
        tile_1 = Tile(1, [line.strip()[:tile_size] for line in lines[:tile_size]], 0, tile_size)
        tile_2 = Tile(2, [line.strip()[tile_size:2 * tile_size] for line in lines[:tile_size]], 0, 2 * tile_size)
        tile_3 = Tile(3, [line.strip()[:tile_size] for line in lines[tile_size:2 * tile_size]], tile_size, tile_size)
        tile_4 = Tile(4, [line.strip()[:tile_size] for line in lines[tile_size * 2:tile_size * 3]], 2 * tile_size, 0)
        tile_5 = Tile(5, [line.strip()[tile_size:2 * tile_size] for line in lines[tile_size * 2:tile_size * 3]],
                      2 * tile_size, tile_size)
        tile_6 = Tile(6, [line.strip()[:tile_size] for line in lines[tile_size * 3:tile_size * 4]], 3 * tile_size, 0)
        instructions = lines[tile_size * 4 + 1]

    curr_tile = tile_1
    tile_1.above = tile_6
    tile_1.left = tile_4
    tile_1.right = tile_2
    tile_1.below = tile_3

    tile_2.above = tile_6
    tile_2.left = tile_1
    tile_2.right = tile_5
    tile_2.below = tile_3

    tile_3.above = tile_1
    tile_3.left = tile_4
    tile_3.right = tile_2
    tile_3.below = tile_5

    tile_4.above = tile_3
    tile_4.left = tile_1
    tile_4.right = tile_5
    tile_4.below = tile_6

    tile_5.above = tile_3
    tile_5.left = tile_4
    tile_5.right = tile_2
    tile_5.below = tile_6

    tile_6.above = tile_4
    tile_6.left = tile_1
    tile_6.right = tile_5
    tile_6.below = tile_2

    return Map(curr_tile, tile_size), instructions
