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

# replaceKthDigit(n, k, d) takes a non-negative int n, a non-negative int k,
# and an int d where 0<=d<=9, and returns the number resulting by replacing
# the kth digit (where k is defined as in kthDigit, above) of the number n
# with the digit d.

def replaceKthDigit(n, k, d):

    # As an example, replace 6 in the number below, with 5.
    # n = 12345 |6| 78901
    #Break the number into two parts using (abs(n) % (10 ** (k + 1))
    # remainder = 678901
    # n - remainder = 12345 000000
    # Divide 678901 into two parts as 6 | 78901
    # remainder2 = 78901
    # New Number = 12345 000000 + 78901 + (5 * 100000)

    # remainder = (abs(n) % (10 ** (k + 1)))
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))=
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    remainder = (abs(n) % (10 ** (k + 1)))
    result    = (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    if n < 0 : result *= -1
    return result

# clearLeftmostDigit(n) takes a non-negative int n and returns the
# number resulting by deleting the leftmost digit.

def clearLeftmostDigit(n):
    numDigit = digitCount(n)
    return replaceKthDigit(n, numDigit - 1, 0)


assert(clearLeftmostDigit(789) == 89)
assert(clearLeftmostDigit(89) == 9)
assert(clearLeftmostDigit(9) == 0)
assert(clearLeftmostDigit(0) == 0)
assert(clearLeftmostDigit(60789) == 789)

