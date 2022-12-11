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

        contained_in_1 = section_2_min >= section_1_min and section_2_max <= section_1_max
        contained_in_2 = section_1_min >= section_2_min and section_1_max <= section_2_max

        if contained_in_1 or contained_in_2:
            count += 1

print(count)
