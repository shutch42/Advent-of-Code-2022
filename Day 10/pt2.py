cycle_operations = []
curr_row = ""
x = 1

with open("input.txt") as file:
    for line in file:
        instructions = line.strip().split(" ")
        instruction = instructions[0]

        if instruction == "noop":
            cycle_operations.append("n")
        if instruction == "addx":
            cycle_operations.append("n")
            cycle_operations.append(instructions[1])

for i, operation in enumerate(cycle_operations):
    cycle = i + 1
    pixel = i % 40

    if pixel == 0:
        print(curr_row)
        curr_row = ""

    if x - 1 <= pixel <= x + 1:
        curr_row += '#'
    else:
        curr_row += '.'

    if operation != "n":
        x += int(operation)

print(curr_row)
