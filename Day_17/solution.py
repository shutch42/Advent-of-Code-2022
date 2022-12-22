from helper import *
movements = []

# Load in movements from text file
with open("input.txt") as file:
    for direction in file.read():
        movements.append(direction)
num_movements = len(movements)


# Simulate 20000 blocks falling, and record the height after each block
curr_height = -1
space = [['.' for _ in range(7)] for _ in range(8)]
move_counter = 0
heights_per_turn = []
for i in range(20000):
    block = None
    if i % 5 == 0:
        block = HorizontalLine(curr_height + 4, 2)
    elif i % 5 == 1:
        block = Plus(curr_height + 4, 2)
    elif i % 5 == 2:
        block = RightAngle(curr_height + 4, 2)
    elif i % 5 == 3:
        block = VerticalLine(curr_height + 4, 2)
    elif i % 5 == 4:
        block = Square(curr_height + 4, 2)

    settled = False
    while not settled:
        curr_movement = movements[move_counter % num_movements]
        move_counter += 1
        leftmost = min(block.pts, key=lambda x: x[1])[1]
        rightmost = max(block.pts, key=lambda x: x[1])[1]

        if curr_movement == '>':
            if rightmost < 6:
                overlap = False
                for pt in block.pts:
                    if space[pt[0]][pt[1] + 1] == '#':
                        overlap = True
                if not overlap:
                    block.move_right()
        elif curr_movement == '<':
            if leftmost > 0:
                overlap = False
                for pt in block.pts:
                    if space[pt[0]][pt[1] - 1] == '#':
                        overlap = True
                if not overlap:
                    block.move_left()

        for pt in block.pts:
            row = pt[0]
            col = pt[1]

            if col > rightmost:
                rightmost = col
            if col < leftmost:
                leftmost = col

            if row - 1 <= curr_height and 0 <= col < 7:
                if space[row - 1][col] == '#' or row == 0:
                    settled = True
                    break
        if not settled:
            block.move_down()

    max_height = max(block.pts, key=lambda x: x[0])[0]
    if max_height > curr_height:
        curr_height = max_height
    heights_per_turn.append((curr_height+1, move_counter, type(block)))

    add_rows = max_height + 8 - len(space)
    for _ in range(add_rows):
        space.append(['.', '.', '.', '.', '.', '.', '.'])

    for pt in block.pts:
        space[pt[0]][pt[1]] = '#'


# print pt1 result
print(heights_per_turn[2021][0])


# calculate pt2 result
moves_per_cycle = 5*num_movements   # 5 blocks * the number of moves total should count the length of a cycle
block_before_cycle = 0
blocks_per_cycle = 0
height_before_cycle = 0
height_per_cycle = 0
height_per_block = []
cycle_found = False

# Start by iterating all heights, and tracking the number of moves made
for i in range(len(heights_per_turn)):
    curr_cycle = heights_per_turn[i][1]
    target_cycle = curr_cycle + moves_per_cycle
    block_type = heights_per_turn[i][2]
    for j in range(i, len(heights_per_turn)):
        # If the cycle number is reached and the turn has the same block type as start of cycle, check and record values
        if heights_per_turn[j][1] == target_cycle and heights_per_turn[j][2] == block_type:
            block_before_cycle = i + 1
            blocks_per_cycle = j - i
            height_before_cycle = heights_per_turn[i-1][0]
            height_per_cycle = heights_per_turn[j][0] - heights_per_turn[i][0]

            # Double check that the cycle is accurate by looking at one more cycle into the future
            if height_per_cycle == heights_per_turn[j + blocks_per_cycle][0] - heights_per_turn[j][0]:
                cycle_found = True
                height_per_block = [heights_per_turn[k][0] - height_before_cycle for k in range(i, j+1)]
                break
    if cycle_found:
        break

# Calculate final height using cycle height, length, and initial value
steps_to_estimate = 1000000000000 - block_before_cycle
height = height_before_cycle + \
         (steps_to_estimate // blocks_per_cycle) * height_per_cycle + \
         height_per_block[steps_to_estimate % blocks_per_cycle]

# Answer for pt2
print(height)

