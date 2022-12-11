import string
letter_priority = {}

for priority, letter in enumerate(string.ascii_lowercase):
    letter_priority[letter] = priority + 1

for priority, letter in enumerate(string.ascii_uppercase):
    letter_priority[letter] = priority + 27

sum_priority = 0
group_bags = []
with open('input.txt') as file:
    for i, line in enumerate(file):
        rucksack = line.strip()
        group_bags.append(rucksack)
        if i % 3 == 2:
            for item in group_bags[0]:
                if item in group_bags[1] and item in group_bags[2]:
                    sum_priority += letter_priority[item]
                    break
            group_bags = []

print(sum_priority)