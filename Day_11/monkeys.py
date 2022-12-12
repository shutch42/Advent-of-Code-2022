class Game:
    def __init__(self, filename, worry_divisor):
        self.monkeys = []
        self.worry_divisor = worry_divisor
        self.product_divisors = 1
        with open(filename) as file:
            monkey_data = file.read().split("\n\n")
            for monkey in monkey_data:
                attributes = monkey.split("\n")

                starting_items = attributes[1].split(": ")[1].split(", ")
                starting_items = [int(i) for i in starting_items]

                operation = attributes[2].split("new = old ")[1]

                test_divisible = int(attributes[3].split("divisible by ")[1])
                self.product_divisors *= test_divisible

                result_monkey_true = int(attributes[4].split("throw to monkey ")[1])
                result_monkey_false = int(attributes[5].split("throw to monkey ")[1])
                self.monkeys.append(
                    Monkey(starting_items, operation, test_divisible, result_monkey_true, result_monkey_false))

    def play_round(self):
        for i in range(len(self.monkeys)):
            while len(self.monkeys[i].items) > 0:
                self.monkeys[i].inspect_item(self.worry_divisor)
                throw_to = self.monkeys[i].test_item_result_monkey(self.product_divisors)
                self.monkeys[throw_to].items.append(self.monkeys[i].items.pop(0))

    def print_monkey_items(self):
        for i, monkey in enumerate(self.monkeys):
            print(f"Monkey {i}: {monkey.items}")

    def print_inspections(self):
        for i, monkey in enumerate(self.monkeys):
            print(f"Monkey {i}: {monkey.num_inspections}")

    def monkey_business_score(self):
        inspections = []
        for monkey in self.monkeys:
            inspections.append(monkey.num_inspections)

        inspections.sort(reverse=True)
        monkey_business = inspections[0] * inspections[1]
        return monkey_business


class Monkey:
    def __init__(self, items, operation, test_divisible, result_monkey_true, result_monkey_false):
        self.items = items
        self.operation = operation
        self.test_divisible = test_divisible
        self.result_monkey_true = result_monkey_true
        self.result_monkey_false = result_monkey_false
        self.num_inspections = 0

    def inspect_item(self, worry_divisor):
        self.num_inspections += 1

        if self.operation[0] == '*':
            num = self.operation.split("* ")[1]
            if num == 'old':
                self.items[0] *= self.items[0]
            else:
                self.items[0] *= int(num)
        else:
            num = self.operation.split("+ ")[1]
            if num == 'old':
                self.items[0] += self.items[0]
            else:
                self.items[0] += int(num)

        self.items[0] = int(self.items[0] / worry_divisor)

    def test_item_result_monkey(self, product_divisors):
        self.items[0] = self.items[0] % product_divisors
        if self.items[0] % self.test_divisible == 0:
            return self.result_monkey_true
        else:
            return self.result_monkey_false
