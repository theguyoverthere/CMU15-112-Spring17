#******************************************************************************#
# Author: Tarique Anwer
# Date:   1/6/2017
# Description: This problem involves the game Sudoku, though we will generalize
#              it to the N^2xN^2 case, where N is a positive integer (and not
#              just the 32x32 case which is most commonly played). First, read
#              the top part (up to History) of the Wikipedia page on Sudoku so
#              we can agree on the rules. As for terminology, we will refer to
#              each of the N^2 different N-by-N sub-regions as "blocks". The
#              following figure shows each of the 9 blocks in a 32x32 puzzle
#              highlighted in a different color:
#
#              Note: this example is 32x32 but your code must work for arbitrary
#              sizes (N^2xN^2 for arbitrary N). For our purposes, we will number
#              the blocks from 0 to N^2-1 (hence, 0 to 8 in the figure), with
#              block 0 in the top-left (in light blue in the figure), moving
#              across and then down (so, in the figure, block 1 is yellow, block
#              2 is maroon, block 3 is red, block 4 is pink, block 5 is gray,
#              block 6 is tan, block 7 is green, and block 8 is sky blue).
#
#              We will refer to the top row as row 0, the bottom row as row
#              (N^2-1), the left column as column 0, and the right column as
#              column (N^2-1).
#
#              A Sudoku is in a legal state if all N4 cells are either blank or
#              contain a single integer from 1 to N^2 (inclusive), and if each
#              integer from 1 to N^2 occurs at most once in each row, each
#              column, and each block. A Sudoku is solved if it is in a legal
#              state and contains no blanks.
#
#              We will represent a Sudoku board as an N^2xN^2 2d list of
#              integers, where 0 indicates that a given cell is blank. For
#              example, here is how we would represent the 32x32 Sudoku board in
#              the figure above:
#              [[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
#               [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
#               [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
#               [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
#               [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
#               [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
#               [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
#               [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
#               [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
#             With this description in mind, your task is to write some
#             functions to indicate if a given Sudoku board is legal. To make
#             this problem more approachable, we are providing a specific design
#             for you to follow. And to make the problem more gradeable, we are
#             requiring that you follow the design! So you should solve the
#             problem by writing the following functions in the order given:
#
#             areLegalValues(values) [10 pts]
#             =====================
#             This function takes a 1d list of values, which you should verify
#             is of length N^2 for some positive integer N and contains only
#             integers in the range 0 to N^2 (inclusive). These values may be
#             extracted from any given row, column, or block in a Sudoko board
#             (and, in fact, that is exactly what the next few functions will do
#             -- they will each call this helper function). The function returns
#             True if the values are legal: that is, if every value is
#             an integer between 0 and N^2, inclusive, and if each integer from
#             1 to N^2 occurs at most once in the given list (0 may be repeated,
#             of course).  Note that this function does not take a 2d Sudoku
#             board, but only a 1d list of values that presumably have been
#             extracted from some Sudoku board.
#
#             isLegalRow(board, row) [10 pts]:
#             ======================
#             This function takes a Sudoku board and a row number. The function
#             returns True if the given row in the given board is legal (where
#             row 0 is the top row and row(N^2-1) is the bottom row), and False
#             otherwise. To do this, your function must create a 1d list of
#             length N^2 holding the values from the given row, and then provide
#             these values to the areLegalValues function you previously wrote.
#             (Actually, because areLegalValues is non-destructive, you do not
#             have to copy the row; you may use an alias.)
#
#             isLegalCol(board, col) [10 pts]:
#             ======================
#             This function works just like the isLegalRow function, only for
#             columns, where column 0 is the leftmost column and column (N^2-1)
#             is the rightmost column. Similarly to isLegalRow, this function
#             must create a 1d list of length N^2 holding the values from the
#             given column, and then provide these values to the areLegalValues
#             function you previously wrote.
#
#             isLegalBlock(board, block) [10 pts]
#             ==========================
#             This function works just like the isLegalRow function, only for
#             blocks, where block 0 is the left-top block, and block numbers
#             proceed across and then down, as described earlier. Similarly to
#             isLegalRow and isLegalCol, this function must create a 1d list of
#             length N^2 holding the values from the given block, and then
#             provide these values to the areLegalValues function you previously
#             wrote.
#
#             isLegalSudoku(board) [10 pts]
#             ====================
#             This function takes a Sudoku board (which you may assume is a
#             N^2xN^2 2d list of integers), and returns True if the board is
#             legal, as described above. To do this, your function must call
#             isLegalRow over every row, isLegalCol over every column, and
#             isLegalBlock over every block. See how helpful those helper
#             functions are? Seriously, this exercise is a very clear
#             demonstration of the principle of top-down design and function
#             decomposition.
#******************************************************************************#
import math

def isPerfectSquare(n):
    """ Determine if an integer is a perfect square.

    :param n: An integer. There is no requirement for the input to be
             a legal integer, though.

    :return: True if the integer is a perfect square. False otherwise
    """
    if (isinstance(n, int) and
            (n >= 0)       and
            (math.floor(math.sqrt(n)) ** 2 == n)):
        return True

    return False

def areLegalValues(values):
    """
    This function takes a 1d list of values, which is of length N^2 for some
    positive integer N and contains only integers in the range 0 to N^2
    (inclusive). These values may be extracted from any given row, column, or
    block in a Sudoko board.

    :param values: A 1d list of values that presumably have been extracted from
                   some Sudoku board.

    :return: The function returns True if the values are legal: that is, if
             every value is an integer between 0 and N^2, inclusive, and if each
             integer from 1 to N^2 occurs at most once in the given list (0 may
             be repeated, of course).
    """

    listRange = len(values)

    if isPerfectSquare(listRange):
        for i in range(listRange):

            if (not isinstance(values[i], int) or
                    (values[i] < 0)            or
                    (values[i] > listRange)    or
                    (values[i] != 0 and values.count(values[i]) > 1)):
                return False

        return True

    return False

def isLegalRow(board, row):
    """
    This function takes a Sudoku board and a row number. The function returns
    True if the given row in the given board is legal (where row 0 is the top
    row and row(N^2-1) is the bottom row), and False otherwise.

    :param board: A 2d list representing a Sudoku board.

    :param row: The row which needs to be verified. Should be between 0 and
                N^2 - 1, however it must be the caller who ensures this.

    :return: True if the given row in the board is legal. False otherwise.
    """

    if areLegalValues(board[row]):
        return True

    return False

def isLegalCol(board, col):
    """
    This function takes a Sudoku board and a column number. The function returns
    True if the given column in the given board is legal (where row 0 is the
    left most column and column (N^2-1) is the extreme right), and False
    otherwise.

    :param board: A 2d list representing a Sudoku board.

    :param col: The column which needs to be verified. Should be between 0 and
                N^2 - 1, however it must be the caller who ensures this.

    :return: True if the given column in the board is legal. False otherwise.
    """
    (rows, columns) = (len(board), len(board[0]))

    extract = []

    for row in range(rows):
            extract.append(board[row][col])

    if areLegalValues(extract):
        return True

    return False

def isLegalBlock(board, block):
    """
    This function takes a Sudoku board and a block number. The function returns
    True if the given block in the given board is legal. The block numbers for
    a 3x3 board would be as follows:

    0 1 2
    3 4 5
    6 7 8

    :param board: A 2d list representing a Sudoku board.

    :param block: The block which needs to be verified. Should be between 0 and
                N, however it must be the caller who ensures this.
    :return: True if the given block in the board is legal. False otherwise.
    """
    
    (rows, columns) = (len(board), len(board[0]))

    #Number of blocks in an NxN board
    N = int(math.sqrt(columns))

    #Coordinates of the top-left corner of the block.
    x0 = math.floor(block / N) * N
    y0 = (block % N) * N

    extract = []
    for row in range(N):
        for column in range(N):
            (xn, yn) = ((x0 + row), (y0 + column))
            extract.append(board[xn][yn])

    if areLegalValues(extract):
        return True

    return False

def areValidRows(board):
    """
    Ensures all the rows in the NxN Sudoku Board are legal.
    :param board: A 2d list representing a Sudoku board.
    :return: True, if all the rows in the board are legal.
    """
    (rows, columns) = (len(board), len(board[0]))

    for row in range(rows):
        if not isLegalRow(board, row):
            return False

    return True

def areValidColumns(board):
    """
    Ensures all the columns in the NxN Sudoku Board are legal.
    :param board: A 2d list representing a Sudoku board.
    :return: True, if all the columns in the board are legal.
    """
    (rows, columns) = (len(board), len(board[0]))

    for column in range(columns):
        if not isLegalCol(board, column):
            return False

    return True

def areValidBlocks(board):
    """
    Ensures all the blocks in the NxN Sudoku Board are legal.
    :param board: A 2d list representing a Sudoku board.
    :return: True, if all the columns in the board are legal.
    """

    (rows, columns) = (len(board), len(board[0]))

    #Number of blocks in an NxN board
    N = int(math.sqrt(columns))

    for block in range(N):
        if not isLegalBlock(board, block):
            return False

    return True

def isLegalSudoku(board):
    """ This function takes a Sudoku board (which you may assume is a N^2xN^2
        2d list of integers), and returns True if the board is legal.
    :param board: A 2d list representing a Sudoku board.
    :return: True, if all the values on the board are legal.
    """

    if (areValidRows(board) and
        areValidColumns(board) and
        areValidBlocks(board)):
        return True

    return False

