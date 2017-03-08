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

# kthDigit(n, k) takes a possibly-negative int value n and a
# non-negative int value k, and returns the kth digit of n,
# counting right-to-left, and 0-based (so the 0th digit is
# the rightmost digit, that is, the 1's digit)

def kthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

# getLeftmostDigit(n) takes a non-negative int n and returns
# the leftmost digit (that is, the one with the highest place value).
def getLeftmostDigit(n):
    numDigits = digitCount(n)
    return kthDigit(n, numDigits - 1)

assert(getLeftmostDigit(7089) == 7)
assert(getLeftmostDigit(89) == 8)
assert(getLeftmostDigit(9) == 9)
assert(getLeftmostDigit(0) == 0)

