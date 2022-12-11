import string
letter_priority = {}

for priority, letter in enumerate(string.ascii_lowercase):
    letter_priority[letter] = priority + 1

for priority, letter in enumerate(string.ascii_uppercase):
    letter_priority[letter] = priority + 27

sum_priority = 0
with open('input.txt') as file:
    for line in file:
        rucksack = line.strip()
        num_items = len(rucksack)
        midpoint = num_items//2
        compartment_1 = rucksack[0:midpoint]
        compartment_2 = rucksack[midpoint:num_items]

        for item in compartment_1:
            if item in compartment_2:
                sum_priority += letter_priority[item]
                break

print(sum_priority)
