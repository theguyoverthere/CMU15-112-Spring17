#******************************************************************************#
# Author: Tarique Anwer
# Date:   3/6/2017
# Description: Background: In Chess, a King can move from any
#              square to any adjacent square in any of the 8 possible
#              directions. A King's Tour is a series of legal King moves so that
#              every square is visited exactly once. We can represent a Kings
#              Tour in a 2d list where the numbers represent the order the
#              squares are visited, going from 1 to N^2.
#
#              For example, consider these 2d lists:
#              [ [  3, 2, 1 ],        [ [  1, 2, 3 ],      [ [ 3, 2, 1 ],
#                [  6, 4, 9 ],          [  7, 4, 8 ],        [ 6, 4, 0 ],
#                [  5, 7, 8 ] ]         [  6, 5, 9 ] ]       [ 5, 7, 8 ] ]
#
#              The first is a legal Kings Tour but the second is not, because
#              there is no way to legally move from the 7 to the 8, and the
#              third is not, because it contains a 0 which is out of range.
#              Also, this should work not just for 3x3 boards but for any NxN
#              board. For example, here is a legal Kings Tour in a 4x4 board:
#
#              [ [  1, 14, 15, 16],
#                [ 13,  2,  7,  6],
#                [ 12,  8,  3,  5],
#                [ 11, 10,  9,  4]
#              ]
#
#              With this in mind, write the function isKingsTour(board) that
#              takes a 2d list of integers, which you may assume is NxN for
#              some N>0, and returns True if it represents a legal Kings Tour
#              and False otherwise.
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
    """ Locate the starting position of the King on the Chess Board. The
    function could very well be used to locate the nth move made on the board.

    :param board: Chess board, represented as a 2d List.
    :param move: The nth move of the King represented as an integer.
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
    Given the current location of the King (x0, y0), look around to see if the
    nextMove can be achieved by one single move of the King. If possible,
    return the location (xn, yn), else (-1, -1) indicating no such location
    exists.

    :param board: The Chess Board represented as a 2d List.
    :param x0: x-coordinate of the Kings's current location
    :param y0: y-coordinate of the King's current location
    :param nextMove: nth move of the King, represented as an integer.
    :return: Location (xn, yn) if a valid move if found, (-1, -1) otherwise.

    """
    direction = [(-1, -1),  (-1, 0),  (-1, +1),
                 (0,  -1),            (0,  +1),
                 (+1, -1),  (+1, 0),  (+1, +1)]

    for movement in direction:
        xn = x0 + movement[0]
        yn = y0 + movement[1]

        if isValidLocation(board, xn, yn) and board[xn][yn] == nextMove:
            board[xn][yn] *= -1
            return xn, yn

    return -1, -1

def isKingsTour(board):
    """
    In Chess, a King can move from any square to any adjacent square in any of
    the 8 possible directions. A King's Tour is a series of legal King moves so
    that every square is visited exactly once. We can represent a Kings Tour in
    a 2d list where the numbers represent the order the squares are visited,
    going from 1 to N^2.

    For example, consider these 2d lists:
         [ [  3, 2, 1 ],        [ [  1, 2, 3 ],      [ [ 3, 2, 1 ],
           [  6, 4, 9 ],          [  7, 4, 8 ],        [ 6, 4, 0 ],
           [  5, 7, 8 ] ]         [  6, 5, 9 ] ]       [ 5, 7, 8 ] ]

    The first is a legal Kings Tour but the second is not, because there is no
    way to legally move from the 7 to the 8, and the third is not, because it
    contains a 0 which is out of range.

    Also, this works not just for 3x3 boards but for any NxN board. For example,
    here is a legal Kings Tour in a 4x4 board:

        [ [  1, 14, 15, 16],
          [ 13,  2,  7,  6],
          [ 12,  8,  3,  5],
          [ 11, 10,  9,  4]
        ]

    The function isKingsTour(board) takes a 2d list of integers, which is NxN
    for some N > 0, and returns True if it represents a legal Kings Tour and
    False otherwise.

    :param board: The Chess Board with the King's Tour marked by integers.
    :return: True if the representation is a valid King's Tour. False,
             otherwise.
    """
    (rows, columns) = (len(board), len(board[0]))

    # Once the entire board has been traversed, ensured that all the numbers
    # from 1 to N^2 were encountered. This is done by matching the expected
    # sum of numbers from 1 to N^2 with the value actually obtained at the end.

    N = rows * columns
    moveTotal = 1
    checkSum = int(N * (N + 1) / 2)

    nextMove = 1

    x0, y0 = locateStartPosition(board, nextMove)
    if not isValidLocation(board, x0, y0):
        return False

    while nextMove < rows * columns:

        #Keep a running track of the sum of values encountered so far.
        nextMove += 1

        moveTotal += nextMove

        # Starting at the current location, (x0, y0) is it possible to
        # reach the co-ordinates of the next move?
        (xn, yn) = getNextLocation(board, x0, y0, nextMove)

        if not isValidLocation(board, xn, yn):
            return False

        (x0, y0) = (xn, yn)

    return moveTotal == checkSum
