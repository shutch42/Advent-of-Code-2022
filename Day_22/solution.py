from input import *


# Pt 1
map_looping, instructions = load_input_pt1()
map_looping.follow_instructions(instructions)
row = map_looping.curr_row + map_looping.curr_tile.row_offset
col = map_looping.curr_col + map_looping.curr_tile.col_offset
direction = map_looping.direction
print(f"Part 1 Password: {1000*row+4*col+direction}")

# Pt 2
map_cube, instructions_cube = load_input_pt2()
map_cube.follow_instructions(instructions_cube)
row = map_cube.curr_row + map_cube.curr_tile.row_offset
col = map_cube.curr_col + map_cube.curr_tile.col_offset
direction = map_cube.direction
print(row, col, direction)
print(f"Part 2 Password: {1000*row+4*col+direction}")
