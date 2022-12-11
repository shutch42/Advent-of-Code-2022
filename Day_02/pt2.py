from helper import *
total_score = 0

with open('input.txt') as file:
    for line in file:
        opponent_move = move_map_opponent[line[0]]
        outcome = outcome_map[line[2]]
        total_score += outcome

        if outcome == DRAW:
            total_score += opponent_move
        elif outcome == LOSE:
            total_score += move_wins[opponent_move]
        else:
            total_score += move_loses[opponent_move]

print(total_score)
