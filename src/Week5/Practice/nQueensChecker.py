#******************************************************************************#
# Author: Tarique Anwer
# Date:   29/5/2017
# Description: Background: The "N Queens" problem asks if we can place N queens
#              on an NxN chessboard such that no two queens are attacking each
#              other. For most values of N, there are many ways to solve this
#              problem. Here, you will write the function nQueensChecker(board)
#              that takes a 2d list of booleans where True indicates a queen is
#              present and False indicates a blank cell, and returns True if
#              this NxN board contains N queens all of which do not attack any
#              others, and False otherwise.
#******************************************************************************#

def multipleQueensAlongRow(board):
    """
    Check if there are queens on the board lying on a row which attack
    each other. This would happen if more than one queen lies on the same
    column on the board.

    :param board: An NxN 2d list consisting of 1s and 0s indicating True and
                  False, where a True indicates a queen is present and False
                  indicates a blank cell.

    :return: True if there are more than one queen on the same row.
    """

    (rows, columns) = (len(board), len(board[0]))

    for row in range(rows):
        if board[row].count(1) > 1:
            return True

    return False

def multipleQueensAlongColumns(board):
    """
    Check if there are queens on the board lying on a column which attack
    each other. This would happen if more than one queen lies on the same
    column on the board.

    :param board: An NxN 2d list consisting of 1s and 0s indicating True and
                  False, where a True indicates a queen is present and False
                  indicates a blank cell.

    :return: True if there are more than one queen on the same column.
    """
    (rows, columns) = (len(board), len(board[0]))

    for column in range(columns):
        count = 0

        for row in range(rows):
            if board[row][column] == 1:
                count += 1
        if count > 1:
            return True

    return False

def multipleQueensOnRightDiagonals(board):
    """
    Check if there are queens on the board lying on a diagonal which attack
    each other. This would happen if more than one queen lies on the same
    diagonal on the board. The diagonal in this case would be slanting up,
    towards the right.

    :param board: An NxN 2d list consisting of 1s and 0s indicating True and
                  False, where a True indicates a queen is present and False
                  indicates a blank cell.

    :return: True if there are more than one queen on the same diagonal,
             slanting to the right.
    """
    (rows, columns) = len(board), len(board[0])

    direction = [(+1, -1), (-1, +1)]
    start = [(0, 0), (rows - 1, 1)]

    # For each diagonal half of the rectangle
    # i.e. (top-left half, bottom-right half)
    for i, half in enumerate([-1, +1]):
        for column in range(columns):

            count = 0

            if half == -1:
                # As we traverse the upper left triangle, the diagonal
                # lengths increase as we move towards the right.
                diagonalLength = column + 1
            else:
                # On the other hand, the diagonal lengths decrease as we
                # traverse the lower right half, moving towards the right.
                diagonalLength = columns - column

            # Traverse the diagonals.
            for d in range(diagonalLength):

                row = start[i][0] + (d * direction[i][0])
                col = column + (d * direction[i][1])

                if board[row][col] == 1:
                    count += 1

            if count > 1:
                return True

    return False

def multipleQueensOnLeftDiagonals(board):
    """
    Check if there are queens on the board lying on a diagonal which attack
    each other. This would happen if more than one queen lies on the same
    diagonal on the board. The diagonal in this case would be slanting up,
    towards the left.

    :param board: An NxN 2d list consisting of 1s and 0s indicating True and
                  False, where a True indicates a queen is present and False
                  indicates a blank cell.

    :return: True if there are more than one queen on the same diagonal,
             slanting to the left.
    """
    (rows, columns) = len(board), len(board[0])

    direction = [(-1, -1), (+1, +1)]
    start = [(rows - 1, 1), (0, 0)]

    # For each diagonal half of the rectangle
    # i.e. (bottom-left half, top-right half)
    for i, half in enumerate([+1, -1]):
        for column in range(columns):

            count = 0

            if half == +1:
                # As we traverse the bottom left triangle, the diagonal
                # lengths increase as we move towards the right.
                diagonalLength = column + 1
            else:
                # On the other hand, the diagonal lengths decrease as we
                # traverse the upper right half, moving towards the right.
                diagonalLength = columns - column

            for d in range(diagonalLength):

                row = start[i][0] + (d * direction[i][0])
                col = column + (d * direction[i][1])

                if board[row][col] == 1:
                    count += 1

            if count > 1:
                return True

    return False

def multipleQueensAlongDiagonals(board):
    """
    Check if there are queens on the board lying on a diagonal which attack
    each other. This would happen if more than one queen lies on the same
    diagonal on the board.

    :param board: An NxN 2d list consisting of 1s and 0s indicating True and
                  False, where a True indicates a queen is present and False
                  indicates a blank cell.

    :return: True if there are more than one queen lying on the same diagonal.
             False otherwise.
    """
    if (multipleQueensOnRightDiagonals(board) or
            multipleQueensOnLeftDiagonals(board)):
        return True

    return False

def isValidNQueensBoard(board):
    """ Check if the N-Queens board is valid.

    Ensure that the board is of NxN type with N number of Queens present,
    irrespective of their location on the board.

    :param board: An NxN 2d list consisting of 1s and 0s indicating True and
                  False, where a True indicates a queen is present and False
                  indicates a blank cell.
    :return: True if the board is NxN with N queens present.
    """

    count = 0
    (rows, columns) = (len(board), len(board[0]))

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == 1:
                count += 1

    if (count != rows) or (rows != columns):
        return False

    return True

def nQueensChecker(board):
    """
    The "N Queens" problem asks if we can place N queens on an NxN chessboard
    such that no two queens are attacking each other.

    The function nQueensChecker(board) takes a 2d list of booleans where True
    indicates a queen is present and False indicates a blank cell, and returns
    True if this NxN board contains N queens all of which do not attack any
    others, and False otherwise.

    :param board: An NxN 2d list consisting of 1s and 0s indicating True and
                  False, where a True indicates a queen is present and False
                  indicates a blank cell.
    :return: Returns True if the NxN board contains N queens, all of which do
             not attack any others, False otherwise.
    """
    if not isValidNQueensBoard(board):
        return False

    if (multipleQueensAlongRow(board)         or
            multipleQueensAlongColumns(board) or
            multipleQueensAlongDiagonals(board)):
       return False

    return True
