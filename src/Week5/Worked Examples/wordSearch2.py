# wordSearch2.py
# This time with a slightly different handling of directions

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):

    (rows, cols) = (len(board), len(board[0]))

    dirNames = [ ["up-left"  ,   "up", "up-right"],
                 ["left"     ,   ""  , "right"   ],
                 ["down-left", "down", "down-right" ] ]

    for i in range(len(word)):

        row = startRow + i * drow
        col = startCol + i * dcol

        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols) or
            (board[row][col] != word[i])):
            return None

    return word, (startRow, startCol), dirNames[drow+1][dcol+1]

def wordSearchFromCell(board, word, startRow, startCol):

    for dRow in [-1, 0, +1]:
        for dCol in [-1, 0, +1]:
            if (dRow != 0) or (dCol != 0):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       dRow, dCol)
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
