from monkeys import Game
monkeys = []

# Part 1
game = Game("input.txt", worry_divisor=3)
for i in range(20):
    game.play_round()

print(game.monkey_business_score())

# Part 2
game = Game("example_input.txt", worry_divisor=1)
for i in range(10000):
    print(i)
    game.play_round()

print(game.monkey_business_score())
