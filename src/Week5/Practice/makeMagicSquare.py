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
    rows = cols = n
    board = [[0] * cols for row in range(rows)]
    return board

print(createBoard(5))

def printBoard(board):
    pass

def getNextLocation(board):
    pass

def makeMove(board, x, y):
    pass

def makeMagicSquare(n):

    if n <= 0 or n % 2 == 0:
        return None

    count = 0
    board = createBoard(n)
    printBoard(board)

    while count < n * n:
        xNext, yNext = getNextLocation(board)

        board = makeMove(board, xNext, yNext)

        printBoard(board)
