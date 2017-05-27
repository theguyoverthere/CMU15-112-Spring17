# wordSearch1.py

def wordSearchFromCellInDirection(board, word, startRow, startCol, dir):

    (rows, cols) = (len(board), len(board[0]))

    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]

    dirNames = [ "up-left"  ,   "up", "up-right",
                 "left"     ,         "right",
                 "down-left", "down", "down-right" ]

    dRow, dCol = dirs[dir]

    for i in range(len(word)):

        row = startRow + i * dRow
        col = startCol + i * dCol

        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols) or
            (board[row][col] != word[i])):
            return None

    return word, (startRow, startCol), dirNames[dir]

def wordSearchFromCell(board, word, startRow, startCol):

    # There are eight directions, in which we search.
    for dir in range(8):
        result = wordSearchFromCellInDirection(board, word,
                                               startRow, startCol, dir)
        if result is not None:
            return result

    return None

def wordSearch(board, word):
    (rows, cols) = (len(board), len(board[0]))

    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)

            if result is not None:
                return result

    return None


def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    print(wordSearch(board, "dog")) # ('dog', (0, 0), 'right')
    print(wordSearch(board, "cat")) # ('cat', (1, 2), 'left')
    print(wordSearch(board, "tad")) # ('tad', (2, 2), 'up-left')
    print(wordSearch(board, "cow")) # None

testWordSearch()
