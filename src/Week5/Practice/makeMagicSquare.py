#******************************************************************************#
# Author: Tarique Anwer
# Date:   27/5/2017
# Description: Write the function makeMagicSquare(n) that takes a positive odd
#              integer n and returns an nxn magic square by following De La
#              Loubere's Method as described here:
#              http://britton.disted.camosun.bc.ca/magicsq/magic.html
#              If n is not a positive odd integer, return None.
#******************************************************************************#
def createBoard(n):
    """ Create an empty Magic Square Board filled with zeros.

    :param n: A positive integer.
    :return: A list of lists i.e. A 2d List representing the Magic Square Board.
    """
    rows = cols = n
    board = [[0] * cols for row in range(rows)]
    return board

def makeMove(board, x, y, move):
    """ Make a move on the Magic Square board.

    :param board: The Magic Square board created earlier.
    :param x: x-coordinate of the current move.
    :param y: y-coordinate of the current move.
    :param move: An integer representing the current move.
    :return: None
    """
    board[x][y] = move

def maxItemLength(a):
    """
    Find the maximum length of items in the Magic Square Board.
    :param a: The Magic Square Board
    :return: Maximum length of items in the board.
    """
    maxLen = 0
    rows, columns = len(a), len(a[0])

    for row in range(rows):
        for column in range(columns):
            maxLen = max(maxLen, len(str(a[row][column])))

    return maxLen

def printBoard(board):
    """
    Print the (formatted) Magic Square board. Note that this is NOT required
    as part of the exercise
    :param board: Magic Square Board
    :return: None
    """
    (rows, cols) = (len(board), len(board[0]))
    fieldWidth = maxItemLength(board)

    formatSpec = "%" + str(fieldWidth) + "s"

    for row in range(rows):
        for column in range(cols):
            print(formatSpec % str(board[row][column]), end=" ")
        print()

def getNextLocation(board, xc, yc):
    """ Find the next location of the move.

    Given the current location, determine the location of the next move. Here
    are the rules which govern the next move.

    1:	Place the first number in the middle cell of the top row.
    2:	Successive numbers are inserted into the square in a diagonal line
        sloping upwards and to the right.
    3:	When the top row is reached, the next number goes in the bottom row as
        if it were directly below the top row.
    4:	When the right hand column is reached, the next number goes in the
        extreme left column as if it were directly to the right of the right
        hand column.
    5:	When a cell is reached that is already filled, or when the top right
        hand cell is reached, the next number drops to the cell directly below.

    :param board: The Magic Square Board
    :param xc: Current move's x-coordinate.
    :param yc: Current move's y-coordinate.
    :return: (x,y) co-ordinate of the next move.
    """
    (rows, cols) = (len(board), len(board[0]))

    xn, yn = xc - 1, yc + 1

    if xn == -1 and yn == cols:
        xn = xc + 1
        yn = yc
    if xn < 0:
        xn += rows
    elif yn > cols - 1:
        yn -= cols
    if board[xn][yn] != 0:
        xn = xc + 1
        yn = yc

    return xn, yn

def makeMagicSquare(n):
    """ Create Magic Square
    Takes a +ve odd integer n and returns an nxn magic square by following De La
    Loubere's Method(http://britton.disted.camosun.bc.ca/magicsq/magic.html

    If n is not a positive odd integer, returns None.

    :param n: A positive odd integer
    :return: A list representing the Magic Square. If n is not a positive odd
             integer however, the function returns None
    """
    if n <= 0 or n % 2 == 0:
        return None

    move = 1
    (x0, y0) = (0, int(n // 2))

    board = createBoard(n)
    makeMove(board, x0, y0, move)

    while move < n * n:
        move += 1
        xn, yn = getNextLocation(board, x0, y0)
        makeMove(board, xn, yn, move)
        (x0, y0) = (xn, yn)

    return board

