from helper import *

# Read data from text file and save as tuples (original index, value)
with open("input.txt") as file:
    for i, line in enumerate(file):
        items.append((i, int(line.strip())))

# Sort all items using move() function
for i in range(len(items)):
    move(i)

# Calculate sum of values at indices 1000, 2000, 3000
item_values = [item[1] for item in items]
zero_index = item_values.index(0)
sum_items = 0
for item_num in [1000, 2000, 3000]:
    coordinates = (item_num+zero_index) % len(item_values)
    sum_items += item_values[coordinates]

print(sum_items)
