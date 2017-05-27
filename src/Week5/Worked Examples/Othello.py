# othello.py
# https://www.youtube.com/watch?v=Ol3Id7xYsY4
#------------------------------------------------------------------------------#
# Create the board with all zeros.
#------------------------------------------------------------------------------#
def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

#------------------------------------------------------------------------------#
# hasMove(board, player) - See if a move is available - This is done by starting
# at empty positions on the board and looking to see if it is possible to make
# a "sandwich".
#------------------------------------------------------------------------------#
def hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))

    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]

    dRow, dCol = dirs[dir]
    i = 1

    while True:
        row = startRow + i * dRow
        col = startCol + i * dCol

        if (row < 0) or (row >= rows) or (col < 0) or (col >= cols):
            return False
        elif board[row][col] == 0:
            # no blanks allowed in a sandwich!
            return False
        elif board[row][col] == player:
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich. For each "slice" of the
            # meat, we increase the counter by 1.
            i += 1

    return i > 1

def hasMoveFromCell(board, player, startRow, startCol):
    (rows, cols) = (len(board), len(board[0]))

    # The search starts at empty positions to see if it is possible to make
    # a sandwich by marking the current position. If we already have the
    # position marked, we will simply skip it.

    if board[startRow][startCol] != 0:
        return False

    # If the current cell is zero, look around to see if it is possible to make
    # the required sandwich configuration.

    for dir in range(8):
        if hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
            return True

    return False

def hasMove(board, player):
    (rows, cols) = (len(board), len(board[0]))

    # Navigate the entire board to see if it is possible to make a move.
    for row in range(rows):
        for col in range(cols):
            if hasMoveFromCell(board, player, row, col):
                return True

    return False

#------------------------------------------------------------------------------#
# Make a move.
#------------------------------------------------------------------------------#
def makeMoveInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))

    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]

    drow, dcol = dirs[dir]
    i = 1

    while True:
        row = startRow + i * drow
        col = startCol + i * dcol

        if board[row][col] == player:
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich, so flip it!
            board[row][col] = player
            i += 1

def makeMove(board, player, startRow, startCol):
    # assumes the player has a legal move from this cell
    (rows, cols) = (len(board), len(board[0]))

    for dir in range(8):
        if hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
            makeMoveInDirection(board, player, startRow, startCol, dir)

    board[startRow][startCol] = player

#------------------------------------------------------------------------------#
# Print Othello Board
#------------------------------------------------------------------------------#
def getPlayerLabel(player):
    labels = ["-", "X", "O"]

    return labels[player]


def printColLabels(board):
    (rows, cols) = (len(board), len(board[0]))

    print("   ", end="") # skip row label

    for col in range(cols):
        print(chr(ord("A") + col)," ", end="")

    print()

def printBoard(board):
    (rows, cols) = (len(board), len(board[0]))

    printColLabels(board)

    for row in range(rows):
        print("%2d " % (row+1), end="")

        for col in range(cols):
            print(getPlayerLabel(board[row][col]), " ", end="")
        print("%2d " % (row+1))

    printColLabels(board)
#------------------------------------------------------------------------------#
# getMove(board, player)
#------------------------------------------------------------------------------#

def isLegalMove(board, player, row, col):
    (rows, cols) = (len(board), len(board[0]))

    if (row < 0) or (row >= rows) or (col < 0) or (col >= cols):
        return False

    return hasMoveFromCell(board, player, row, col)

def getMove(board, player):
    print()
    printBoard(board)

    while True:
        prompt = "Enter move for player " + getPlayerLabel(player) + ": "
        move = input(prompt).upper()

        # move is something like "A3"
        if ((len(move) != 2) or
            (not move[0].isalpha()) or
            (not move[1].isdigit())):
            print("Wrong format!  Enter something like A3 or D5.")
        else:
            col = ord(move[0]) - ord('A')
            row = int(move[1]) - 1

            if not isLegalMove(board, player, row, col):
                print("That is not a legal move!  Try again.")
            else:
                return row, col
#------------------------------------------------------------------------------#
# Play the Game
#------------------------------------------------------------------------------#
def playOthello(rows, cols):

    # create initial board
    board = make2dList(rows, cols)

    board[rows // 2][cols // 2] = board[rows // 2 - 1][cols // 2 - 1] = 1
    board[rows // 2 - 1][cols // 2] = board[rows // 2][cols // 2 - 1] = 2

    (currentPlayer, otherPlayer) = (1, 2)

    # and play until the game is over
    while True:

        if not hasMove(board, currentPlayer):
            if hasMove(board, otherPlayer):
                print("No legal move!  PASS!")
                (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
            else:
                print("No more legal moves for either player!  Game over!")
                break

        (row, col) = getMove(board, currentPlayer)

        makeMove(board, currentPlayer, row, col)

        (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)

    print("Goodbye!")

playOthello(4,4)
