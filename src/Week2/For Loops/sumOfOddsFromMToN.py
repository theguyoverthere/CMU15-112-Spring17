# Version 1
# ---------

def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(m, n + 1):
        if (x % 2) == 1:
            total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# Version 2
# ---------

def sumOfOddsFromMToN(m, n):
    total = 0
    if m % 2 == 0:
        m += 1

    for x in range(m, n + 1, 2):
        total += x

    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))


# Version 3
# ---------
def sumOfOddsFromMToN(m, n):
    total = 0
    if n % 2 == 0: n -= 1

    for x in range(n, m - 1, -2):  # Note when looping down, add -1 to the range
        total += x

    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# Version 4
# ---------
def sumOfOddsFromMtoN(m, n):
    if m % 2 == 0 : m += 1

    return sum(range(m, n + 1, 2))


print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# Version 5
# ---------
# This is the worst way so far -- too confusing.

def sumOfOddsFromMToN(m, n):
    return sum(range(m + (1 - m % 2), n + 1, 2)) # this works, but it's gross!

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))
