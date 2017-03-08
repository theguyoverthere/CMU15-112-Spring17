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

assert(replaceKthDigit(789, 0, 6) == 786)
assert(replaceKthDigit(789, 1, 6) == 769)
assert(replaceKthDigit(789, 2, 6) == 689)
assert(replaceKthDigit(789, 3, 6) == 6789)
assert(replaceKthDigit(789, 4, 6) == 60789)