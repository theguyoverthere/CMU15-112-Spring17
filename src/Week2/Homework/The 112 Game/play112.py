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

def kthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

# getLeftmostDigit(n) takes a non-negative int n and returns
# the leftmost digit (that is, the one with the highest place value).

def getLeftmostDigit(n):
    numDigits = digitCount(n)
    return kthDigit(n, numDigits - 1)

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

# isFull(board) takes a board as specified above and returns True
# if that board is full (no empty spaces), and False otherwise.

def isFull(board):
    while board > 0:
        if board % 10 == 8:
            return False

        board //= 10
    return True


#  isWin(board) takes a board as specified above and returns
#  True if that board is a win (contains 112), and False otherwise.

def isWin(board):
    # Loop while the board size is greater than 2
    while board > 99:
        if kthDigit(board, 0) == 2 and kthDigit(board, 1) == 1 and kthDigit(board, 2) == 1:
            return True
        board //= 10

    return False

# Takes a positive integer number of moves, and returns
# an empty board(all 8's) for a game with that many moves.

def makeBoard(moves):
    board = 0

    for i in range(moves):
        board += 8 * (10 ** i)

    return board

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

def play112(game):
    playerTurn = 0
    boardSize  = getLeftmostDigit(game)
    game       = clearLeftmostDigit(game)
    board      = makeBoard(boardSize)

    if game == 0:
        return "88888: Unfinished!"

    while game > 0:
        #Alternate between two players
        playerTurn += 1

        if playerTurn == 3:
            playerTurn = 1

        #Get next move to be made
        position = getLeftmostDigit(game)
        game     = clearLeftmostDigit(game)
        move     = getLeftmostDigit(game)

        #If the board is not already full, make the move
        if isFull(board):
            break
        else:
            prevBoard = board
            board     = makeMove(prevBoard, position, move)

            if isinstance(board, int): #Successful move
                if isWin(board):
                    return str(board) + ": Player " + str(playerTurn) + " wins!"
            else: #Unsuccessful move
                return str(prevBoard) + ":" + " Player " + str(playerTurn) + ": " + board

        game = clearLeftmostDigit(game)

    if isWin(board):
        return str(board) + ": Player " + str(playerTurn) + " wins!"
    else:
        if isFull(board):
            return str(board) + ": Tie!"
        else:
            return str(board) + ": Unfinished!"

assert(play112( 5 ) == "88888: Unfinished!")
assert(play112( 521 ) == "81888: Unfinished!")
assert(play112( 52112 ) == "21888: Unfinished!")
assert(play112( 5211231 ) == "21188: Unfinished!")
assert(play112( 521123142 ) == "21128: Player 2 wins!")
assert(play112( 521123151 ) == "21181: Unfinished!")
assert(play112( 52112315142 ) == "21121: Player 1 wins!")
assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
assert(play112( 51211 ) == "28888: Player 2: occupied!")
assert(play112( 5122221 ) == "22888: Player 1: occupied!")
assert(play112( 51261 ) == "28888: Player 2: offboard!")
assert(play112( 51122324152 ) == "12212: Tie!")