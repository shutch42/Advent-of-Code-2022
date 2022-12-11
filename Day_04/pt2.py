count = 0

with open('input.txt') as file:
    for line in file:
        assignments = line.strip().split(",")
        elf_1 = assignments[0]
        elf_2 = assignments[1]

        sections_1 = elf_1.split("-")
        sections_2 = elf_2.split("-")

        section_1_min = int(sections_1[0])
        section_2_min = int(sections_2[0])
        section_1_max = int(sections_1[1])
        section_2_max = int(sections_2[1])

        if not (section_1_max < section_2_min or section_2_max < section_1_min):
            count += 1

print(count)
