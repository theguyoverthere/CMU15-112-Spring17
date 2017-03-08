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

# kthDigit(n, k) takes a possibly-negative int value n and a
# non-negative int value k, and returns the kth digit of n,
# counting right-to-left, and 0-based (so the 0th digit is
# the rightmost digit, that is, the 1's digit)

def kthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

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

# makeMove takes a board as specified above, an int position on the board
# (where 1 is the leftmost position), and an int move (1 or 2), and returns
# the new board that results by making the given move in the given position.
#
# If the move is illegal, however, the function instead returns a specific
# error message indicating the nature of the problem.
#
# In particular, if the move is not a 1 or a 2, returns "move must be 1 or 2!".
# If the position is not on the board, returns "offboard!".
# If the position is not empty, return "occupied!".

def makeMove(board, position, move):
    boardSize = digitCount(board)

    if not (move == 1 or move == 2):
        return "move must be 1 or 2!"
    elif position > boardSize:
        return "offboard!"
    elif not kthDigit(board, boardSize - position) == 8:
        return "occupied!"
    else:
        return replaceKthDigit(board, boardSize - position, move)


assert(makeMove(8, 1, 1) == 1)
assert(makeMove(888888, 1, 1) == 188888)
assert(makeMove(888888, 2, 1) == 818888)
assert(makeMove(888888, 5, 2) == 888828)
assert(makeMove(888888, 6, 2) == 888882)
assert(makeMove(888888, 6, 3) == "move must be 1 or 2!")
assert(makeMove(888888, 7, 1) == "offboard!")
assert(makeMove(888881, 6, 1) == "occupied!")
