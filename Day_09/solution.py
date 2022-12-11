from helper import Rope

rope_1 = Rope(2)
rope_2 = Rope(10)

with open("input.txt") as file:
    for line in file:
        instructions = line.strip().split(" ")
        direction = instructions[0]
        num_steps = int(instructions[1])

        for i in range(num_steps):
            if direction == 'R':
                rope_1.move_right()
                rope_2.move_right()
            elif direction == 'U':
                rope_1.move_up()
                rope_2.move_up()
            elif direction == 'L':
                rope_1.move_left()
                rope_2.move_left()
            else:
                rope_1.move_down()
                rope_2.move_down()

# Part 1
print(len(rope_1.tail_positions))

# Part 2
print(len(rope_2.tail_positions))
