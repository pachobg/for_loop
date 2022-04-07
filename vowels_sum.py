word = input()

letter_sum = 0

for i in range(0, len(word)):
    if word[i] == "a":
        letter_sum += 1
    elif word[i] == "e":
        letter_sum += 2
    elif word[i] == "i":
        letter_sum += 3
    elif word[i] == "o":
        letter_sum += 4
    elif word[i] == "u":
        letter_sum += 5
    else:
        letter_sum += 6


print(letter_sum)