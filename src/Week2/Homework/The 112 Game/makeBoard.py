# Takes a positive integer number of moves, and returns
# an empty board(all 8's) for a game with that many moves.

def makeBoard(moves):
    board = 0

    for i in range(moves):
        board += 8 * (10 ** i)

    return board

assert(makeBoard(1) == 8)
assert(makeBoard(2) == 88)
assert(makeBoard(3) == 888)