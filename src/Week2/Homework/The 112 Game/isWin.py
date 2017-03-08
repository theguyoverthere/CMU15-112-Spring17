def kthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

#  isWin(board) takes a board as specified above and returns
#  True if that board is a win (contains 112), and False otherwise.
def isWin(board):
    # Loop while the board size is greater than 2
    while board > 99:
        if kthDigit(board, 0) == 2 and kthDigit(board, 1) == 1 and kthDigit(board, 2) == 1:
            return True
        board //= 10

    return False

assert(isWin(888888) == False)
assert(isWin(112888) == True)
assert(isWin(112888) == True)
assert(isWin(888112) == True)
assert(isWin(211222) == True)
assert(isWin(212212) == False)
