def duplicates(window):
    for i, char in enumerate(window):
        if char in window[i+1:len(window)]:
            return True
    return False


with open("input.txt") as file:
    signal = file.read()
    window = signal[0:14]
    last_char = 14
    while duplicates(window):
        last_char += 1
        window = signal[last_char-14:last_char]

    print(window)
    print(last_char)
