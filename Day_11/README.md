# Part 2 Explaination 🐒  
Part 2 of this problem is significantly more difficult than part 1. Since integers have a maximum value, the number value of each item is not able to be contained in an integer when the program is run for many rounds. Because of this, we have to do a bit of math to contain the same info about each item in a smaller number.  
  
First, we should establish the goal of this program:
1. We are not really tracking the stress level associated with each item, we are only using the stress level to determine which monkey an item will be passed to.
2. We only wish to track the number of items inspected per monkey.

Therefore, the goal for this part of the program is find a lower number for each item that will still allow the item to follow the same path between monkeys.  

In order for an item to follow the same path, it must have the same result after each monkey's test. Each test checks if the item number is divisible by a value associated with each monkey.  
  
We can check this using a modulo:  
item % divisor == remainder,  
where the remainder determines where the item will go next.  

As long as this remainder stays accurate for each monkey, we can lower the value of the items being thrown around.  
For example-  
item % divisor_monkey1 == lower_item % divisor_monkey1 == remainder_monkey1  
item % divisor_monkey2 == lower_item % divisor_monkey2 == remainder_monkey2  
item % divisor_monkey3 == lower_item % divisor_monkey2 == remainder_monkey3,  
and so on.  

The exact value of each item does not matter, as long as each remainder is the same.  
  
Since the only operations on each number are addition and multiplication, the smaller number should get the same result after the modulo operation. This is because addition and multiplication are closed under modulus.  
  
For example,  
If x % divisor = r,  
then x % divisor = r % divisor,  
  
And when we add a number n to x,  
(x + n) % divisor = (r + n) % divisor  
  
If we multiply a number n by x,
(x * n) % divisor = (r * n) % divisor

Since the remainder r is the same for a smaller x, multiplying and adding values to this number should give us the same remainder after the monkey inspects each item (adding or multiplying the value).  
  
So now, we just need to figure out the smaller value for x.  
  
Since x just needs to be a value with the same remainder for the divisor associated with each monkey, we can bring this number down by subtracting a number that is divisible in all of the monkeys tests.  
For example,  
If the monkeys are using divisors of 2, 5, 7, and 9, then what number is divisible by all of these numbers? Well, the easiest solution is to just multiply all of these numbers together.  
2 * 5 * 7 * 9 = 630, so a value of 630 will result in a remainder of zero for each monkey. Therefore, subtracting this value from each item will result in the same remainder for each test.  
  
To make each item as small as possible, we should subtract this number as many times as we can from each item. Another way to do this is just to use modulo.  
  
So for each item,  
(A smaller, equivalent item) = (the item number) % (product of all monkey divisors)  
  
If you keep reducing the item using this method each round, the number will remain small enough to store in an integer and complete all rounds of the game.  

The code that implements this method is contained in [monkeys.py](https://github.com/shutch42/Advent-of-Code-2022/blob/main/Day_11/monkeys.py).  
