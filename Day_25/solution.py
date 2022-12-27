total_decimal = 0

# Read SNAFU numbers from file and convert to decimal
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        decimal_val = 0
        for i in range(len(line)):
            snafu_code = line[len(line)-1-i]
            multiplier = 5**i
            if snafu_code == '-':
                decimal_val -= multiplier
            elif snafu_code == '=':
                decimal_val -= 2*multiplier
            else:
                snafu_code = int(snafu_code)
                decimal_val += snafu_code*multiplier
        total_decimal += decimal_val

# Convert total decimal number back to SNAFU digits
quotient = total_decimal
next_digit = 0
snafu_digits = []
while quotient != 0:
    remainder = quotient % 5 + next_digit
    if remainder == 3:
        snafu_digits.insert(0, -2)
        next_digit = 1
    elif remainder == 4:
        snafu_digits.insert(0, -1)
        next_digit = 1
    elif remainder == 5:
        snafu_digits.insert(0, 0)
        next_digit = 1
    else:
        snafu_digits.insert(0, remainder)
        next_digit = 0
    quotient = quotient // 5

#  Convert SNAFU digits to a string with - and =
snafu_str = ""
for digit in snafu_digits:
    if digit == -1:
        snafu_str += '-'
    elif digit == -2:
        snafu_str += '='
    else:
        snafu_str += str(digit)

print(snafu_str)
