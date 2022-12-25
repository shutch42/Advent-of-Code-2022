from input import *


def test_example_pt1():
    map_ex1, instructions_ex1 = load_example_pt1()
    map_ex1.follow_instructions(instructions_ex1)
    row = map_ex1.curr_row + map_ex1.curr_tile.row_offset
    col = map_ex1.curr_col + map_ex1.curr_tile.col_offset
    direction = map_ex1.direction
    return 1000*row + 4*col + direction == 6032


def test_example_pt2():
    map_ex2, instructions_ex2 = load_example_pt2()
    map_ex2.follow_instructions(instructions_ex2)
    row = map_ex2.curr_row + map_ex2.curr_tile.row_offset
    col = map_ex2.curr_col + map_ex2.curr_tile.col_offset
    direction = map_ex2.direction
    return 1000*row + 4*col + direction == 5031
