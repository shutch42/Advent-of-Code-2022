ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

move_map_opponent = {'A': ROCK,
                     'B': PAPER,
                     'C': SCISSORS}

move_map_player = {'X': ROCK,
                   'Y': PAPER,
                   'Z': SCISSORS}

outcome_map = {"X": LOSE,
               "Y": DRAW,
               "Z": WIN}

move_wins = {ROCK: SCISSORS,
             SCISSORS: PAPER,
             PAPER: ROCK}

move_loses = {ROCK: PAPER,
              PAPER: SCISSORS,
              SCISSORS: ROCK}
