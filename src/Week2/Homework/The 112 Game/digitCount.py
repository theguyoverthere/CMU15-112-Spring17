# digitCount(n) takes a possibly-negative int value n
# and returns the number of digits in n

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

assert(digitCount(0) == 1)
assert(digitCount(5) == digitCount(-5) == 1)
assert(digitCount(42) == digitCount(-42) == 2)
assert(digitCount(121) == digitCount(-121) == 3)