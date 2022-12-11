from helper import *
total_score = 0

with open('input.txt') as file:
    for line in file:
        opponent_move = move_map_opponent[line[0]]
        my_move = move_map_player[line[2]]
        total_score += my_move

        if my_move == opponent_move:
            total_score += DRAW
        elif move_wins[my_move] == opponent_move:
            total_score += WIN

print(total_score)
