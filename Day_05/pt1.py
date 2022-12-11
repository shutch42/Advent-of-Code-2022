import os
import time

NUM_STACKS = 9
crate_lists = [[] for i in range(NUM_STACKS)]


# This function generates frames for an animation of the movement of the crates
def print_stacks(stacks):
    os.system('clear')
    lines = [""]*60

    lines[0] = "CrateMover 9000"
    for i in range(NUM_STACKS):
        lines[2] += f" {i+1}   "

    curr_level = 3
    num_matches = 1
    while num_matches > 0:
        num_matches = 0
        for i in range(NUM_STACKS):
            if curr_level-3 < len(stacks[i]):
                num_matches += 1
                lines[curr_level] += f"[{stacks[i][curr_level-3]}]  "
            else:
                lines[curr_level] += "     "
        curr_level += 1

    lines.reverse()
    for line in lines:
        print(line.center(80))
    time.sleep(.05)


with open('input.txt') as file:
    sections = file.read().split("\n\n")
    crate_levels = sections[0].split("\n")
    instructions = sections[1].split("\n")

    # Read crates from bottom to top, remove labels
    crate_levels.reverse()
    crate_levels.pop(0)

    for level in crate_levels:
        for i in range(NUM_STACKS):
            if 1+i*4 < len(level):
                crate = level[1+i*4]
                if crate != ' ':
                    crate_lists[i].append(crate)

    print_stacks(crate_lists)

    # Remove blank like from end of instructions
    instructions.pop()

    for instruction in instructions:
        instruction = instruction.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ')
        procedure = instruction.split(' ')
        num_crates = int(procedure[0])
        initial_stack = int(procedure[1]) - 1
        new_stack = int(procedure[2]) - 1

        for i in range(num_crates):
            crate_to_move = crate_lists[initial_stack].pop()
            crate_lists[new_stack].append(crate_to_move)
            print_stacks(crate_lists)

# Solution printed below
print("Top Crates:")
top_crates = ""
for i in range(NUM_STACKS):
    top_crates += crate_lists[i].pop()

print(top_crates)
