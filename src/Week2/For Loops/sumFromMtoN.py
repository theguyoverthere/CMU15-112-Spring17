# Version 1
# ---------
def sumFromMtoN(m, n):
    total = 0
    # note the range (x, y) includes x but excludes y

    for x in range(m, n + 1):
        total += x

    return total

print(sumFromMtoN(5, 10) == 5 + 6 + 7 + 8 + 9 + 10)

# Version 2
# ---------
def sumFromMtoN(m, n):
    total = 0
    # note the range (x, y) includes x but excludes y
    return sum(range(m, n + 1))

print(sumFromMtoN(5, 10) == 5 + 6 + 7 + 8 + 9 + 10)

# Version 3
# ---------
def sumToN(n):
    return n * (n + 1)// 2

def sumFromMtoN(m, n):
    return sumToN(n) - sumToN(m - 1)

print(sumFromMtoN(5, 10) == 5 + 6 + 7 + 8 + 9 + 10)

