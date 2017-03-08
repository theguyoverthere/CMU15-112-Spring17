# kthDigit(n, k) takes a possibly-negative int value n and a
# non-negative int value k, and returns the kth digit of n,
# counting right-to-left, and 0-based (so the 0th digit is
# the rightmost digit, that is, the 1's digit)

def kthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)
