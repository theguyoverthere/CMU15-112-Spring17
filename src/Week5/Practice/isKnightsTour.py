#******************************************************************************#
# Author: Tarique Anwer
# Date:   28/5/2017
# Description: Background:  A "knight's tour in chess is a sequence of legal
#              knight moves such that the knight visits every square exactly
#              once. We can represent a (supposed) knight's tour as an NxN list
#              of the integers from 1 to N2 listing the positions in order that
#              the knight occupied on the tour.  If it is a legal knight's tour,
#              then all the numbers from 1 to N2 will be included and each move
#              from k to (k+1) will be a legal knight's move. With this in mind,
#              write the function isKnightsTour(board) that takes such a 2d list
#              of integers and returns True if it represents a legal knight's
#              tour and False otherwise.
#******************************************************************************#
def isValidLocation(board, x, y):
    (rows, columns) = (len(board), len(board[0]))

    if (x < 0) or (y < 0) or (x > columns - 1) or (y > rows - 1):
        return False

    return True

def locateStartPosition(board, move):
    (rows, columns) = (len(board), len(board[0]))

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == 1:
                board[row][column] *= -1
                return row, column

    return -1, -1


def getNextLocation(board, x0, y0, nextMove):
    direction = [        (-2, -1),  (-2, +1),
                 (-1, -2),                   (-1, +2),
                              # Knight#
                 (+1, -2),                   (+1, +2),
                         (+2, -1),  (+2, +1)]

    for movement in direction:
        xn = x0 + movement[0]
        yn = y0 + movement[1]

        if isValidLocation(board, xn, yn) and board[xn][yn] == nextMove:
            board[xn][yn] *= -1
            return xn, yn

    return -1, -1

def isKnightsTour(board):
    (rows, columns) = (len(board), len(board[0]))

    nextMove = 1
    x0, y0 = locateStartPosition(board, nextMove)
    if not isValidLocation(board, x0, y0):
        return False

    while nextMove < rows * columns - 1:
        nextMove += 1

        # Starting at the current location, (x0, y0) is it possible to
        # reach the co-ordinates of the next move?
        (xn, yn) = getNextLocation(board, x0, y0, nextMove)

        if not isValidLocation(board, xn, yn):
            return False

        (x0, y0) = (xn, yn)

    return True
