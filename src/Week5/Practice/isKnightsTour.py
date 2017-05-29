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
    """ Check if the move is a valid move i.e. the location (x, y) is a location
        on the given Chess board.
    :param board: The Chess Board represented as a 2d List
    :param x: x-coordinate of the move.
    :param y: y-coordinate of the move.
    :return: True, if the location of the move is within the valid boundaries.
             False, otherwise!
    """
    (rows, columns) = (len(board), len(board[0]))

    if (x < 0) or (y < 0) or (x > columns - 1) or (y > rows - 1):
        return False

    return True

def locateStartPosition(board, move):
    """ Locate the starting position of the Knight on the Chess Board.

    :param board: Chess board, represented as a 2d List.
    :param move: The nth move of the Knight represented as an integer. Since
                 we're going to locate the starting position, move will be 1.
    :return: Location (row, column) of the nth move. If no such move exists on
             the board, (-1, -1) is returned.
    """
    (rows, columns) = (len(board), len(board[0]))

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == move:
                board[row][column] *= -1
                return row, column

    return -1, -1


def getNextLocation(board, x0, y0, nextMove):
    """
    Given the current location of the Knight (x0, y0), look around to see if the
    nextMove can be achieved by one single move of the Knight. If possible,
    return the location (xn, yn), else (-1, -1) indicating no such location
    exists.

    :param board: The Chess Board represented as a 2d List.
    :param x0: x-coordinate of the Knight's current location
    :param y0: y-coordinate of the Knight's current location
    :param nextMove: nth move of the Knight, represented as an integer.
    :return: Location (xn, yn) if a valid move if found, (-1, -1) otherwise.

    """
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
    """ Determine if the given sequence on a Chess Board is a Knight's Tour.

    A knight's tour in chess is a sequence of legal knight moves such that the
    knight visits every square exactly. We can represent a (supposed) knight's
    tour as an NxN list of the integers from 1 to N2 listing the positions in
    order that the knight occupied on the tour.  If it is a legal knight's tour,
    then all the numbers from 1 to N2 will be included and each move from k to
    (k+1) will be a legal knight's move. The function isKnightsTour(board) takes
    such a a 2d list of integers and returns True if it represents a legal
    knight's tour and False otherwise.

    :param board: The Chess Board with the Knight's Tour marked by integers.
    :return: True if the representation is a valid Knight's Tour. False,
             otherwise.
    """
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
