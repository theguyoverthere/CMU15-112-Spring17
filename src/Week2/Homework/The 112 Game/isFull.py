# isFull(board) takes a board as specified above and returns True
# if that board is full (no empty spaces), and False otherwise.

def isFull(board):
    while board > 0:
        if board % 10 == 8:
            return False

        board //= 10
    return True

assert(isFull(888888) == False)
assert(isFull(121888) == False)
assert(isFull(812188) == False)
assert(isFull(888121) == False)
assert(isFull(212122) == True)
assert(isFull(212212) == True)
