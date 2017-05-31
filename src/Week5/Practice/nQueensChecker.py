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
    (rows, columns) = (len(board), len(board[0]))

    for row in range(rows):
        if board[row].count(1) > 1:
            return True

    return False

def multipleQueensAlongColumns(board):
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
    (rows, columns) = len(board), len(board[0])

    direction = [(-1, -1), (+1, +1)]
    start = [(rows - 1, 1), (0, 0)]

    # For each diagonal half of the rectangle
    # i.e. (bottom-left half, top-right half)
    for i, half in enumerate([+1, -1]):
        for column in range(columns):

            count = 0

            if half == +1:
                diagonalLength = column + 1
            else:
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
    if (multipleQueensOnRightDiagonals(board) or
        multipleQueensOnLeftDiagonals(board)):
        return True

    return False

def nQueensChecker(board):
    if (multipleQueensAlongRow(board)     or
        multipleQueensAlongColumns(board) or
        multipleQueensAlongDiagonals(board)):
       return False

    return True
