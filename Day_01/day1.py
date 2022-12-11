calories_per_elf = []
calories = 0

with open('input.txt') as file:
	for line in file:
		if line == "\n":
			calories_per_elf.append(calories)
			calories = 0
		else:
			calories += int(line)

calories_per_elf.sort(reverse=True)

# Pt. 1
print(calories_per_elf[0])

# Pt. 2
print(sum(calories_per_elf[0:3]))

