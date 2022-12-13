from search import get_path, print_path
import os

initial_node = ()
target_node = ()
row = []
height_map = []
low_nodes = []

with open("input.txt") as file:
    for i, line in enumerate(file):
        for j, char in enumerate(line.strip()):
            if char == 'S':
                initial_node = (i, j)
                height = 1.5    # Use a different height to classify S in printing
            elif char == 'E':
                target_node = (i, j)
                height = 25.5   # Same idea
            elif char == 'a':
                low_nodes.append((i, j))
                height = 1
            else:
                height = ord(char) - 96
            row.append(height)
        height_map.append(row)
        row = []

# Part 1
print_path(initial_node, target_node, height_map)
steps = len(get_path(initial_node, target_node, height_map)) - 1
print(f"Steps Required: {steps}")
print(f"Press Enter to continue")
input()

# Part 2
steps = len(get_path(initial_node, target_node, height_map))
min_length = steps
start_point = initial_node
for i, starting_node in enumerate(low_nodes):
    print(f"Testing start point {i}")
    curr_length = len(get_path(starting_node, target_node, height_map)) - 1
    if curr_length != 0 and curr_length > min_length:
        min_length = curr_length
        start_point = starting_node
os.system('clear')
print_path(start_point, target_node, height_map)
print(f"Steps Required: {min_length}")
