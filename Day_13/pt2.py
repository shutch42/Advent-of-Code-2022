from helper import *
from functools import cmp_to_key

packets = [[[2]], [[6]]]
with open("input.txt") as file:
    pairs = file.read().split("\n\n")
    for i, pair in enumerate(pairs):
        curr_packets = pair.split("\n")
        packets.append(eval(curr_packets[0]))
        packets.append(eval(curr_packets[1]))

packets.sort(key=cmp_to_key(compare))

divider_1 = packets.index([[2]]) + 1
divider_2 = packets.index([[6]]) + 1

print(divider_1 * divider_2)
