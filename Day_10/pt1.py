cycle_operations = []
watch_cycles = [20, 60, 100, 140, 180, 220]
x = 1
sum_signal_strengths = 0

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
    print(f"{cycle}: {x}")

    if cycle in watch_cycles:
        sum_signal_strengths += x*cycle

    if operation != "n":
        x += int(operation)

print(sum_signal_strengths)
