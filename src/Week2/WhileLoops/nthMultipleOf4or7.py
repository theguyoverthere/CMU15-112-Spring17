def isMultipleOf4or7(x):
    return ((x % 4) == 0) or ((x % 7) == 0)


def nthMultipleOf4or7(n):
    found = 0
    guess = -1 # 0 is a multiple of all integers. Hence initialized to -1

    # Keep iterating and each time a multiple is found, make note of it.
    # Once the nth, value is found, return the guess.

    while found <= n:
        guess += 1
        if isMultipleOf4or7(guess):
            found += 1
    return guess

print("Multiples of 4 or 7: ", end="")
for n in range(15):
    print(nthMultipleOf4or7(n), end=" ")
print()