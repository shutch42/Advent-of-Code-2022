from helper import *

sum_indices = 0
with open("input.txt") as file:
    pairs = file.read().split("\n\n")
    for i, pair in enumerate(pairs):
        packets = pair.split("\n")
        list1 = eval(packets[0])
        list2 = eval(packets[1])
        pair_num = i + 1
        if compare(list1, list2) != 1:
            sum_indices += pair_num

print(sum_indices)
