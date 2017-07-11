#******************************************************************************#
# Author: Tarique Anwer
# Date:   11/7/2017
# Description: Write the function playGame42(rows, cols) that takes the
#              dimensions of a board and displays a game of "42" in a
#              suitably-sized window containing a board of those dimensions.
#
#              The game of 42, invented here (and not especially enthralling),
#              works as such:
#              1. The board starts empty.
#              2. Two players (one blue, the other orange) take turns moving.
#                 The UI should always make clear whose turn it is.
#              3. The only event that is used is keyPressed. Your mousePressed
#                 and timerFired functions should simply pass, as in the
#                 starter code.
#              4. At any time, a single cell in the board is highlighted. The
#                 current player can change the highlighted cell with the up,
#                 down, left, and right arrows (with wraparound, so for example,
#                 pressing the left arrow with the selection in the leftmost
#                 column causes the selection to move to the rightmost column in
#                 the same row).
#              5. To make a move, the current player can press a single digit
#                 key. If the current selection is empty, that digit is
#                 displayed in the currently selected cell, using the current
#                 player's color. Otherwise, if the current selection is not
#                 empty, the current player loses that round.
#              6. When a digit is placed, the players "turn sum" is the sum of
#                 all the digits neighboring that digit, plus the digit itself.
#                 If the "turn sum" equals 42, the player wins that round!
#                 Otherwise, play continues with the other player's turn.
#              7. If the board is full and no more moves remain, then the player
#                 with the turn sum in that round that was closest to 42 wins
#                 that round. If there is a tie, the round is a draw and each
#                 player wins 1 point for the round. At the end of each round,
#                 the score is updated, and the board is cleared and the next
#                 round begins.
#              8. A score should be displayed, 1 point per round, first to 5
#                 wins the game.
#              9. When the game is over, the message "Game Over" should be
#                 displayed, and the score should make it clear which player
#                 won, and all further keypresses should be ignored.
#
#              Note: so long as you follow the rules above, there are many tiny
#              details left unanswered here (how large should the board be?
#              where does the score go? what font for the score? etc, etc, etc).
#              You have to decide them for yourself. Do not ask on piazza, do
#              not ask at OH. Just decide. Keep it simple. We are not looking
#              for anything amazing here, just a simple playable game that
#              follows the rules above. Have fun!
#******************************************************************************#
from tkinter import Tk, Canvas, ALL

CELL_SIZE = 50
GRID_MARGIN = (2 / 5) * CELL_SIZE
SCORE_DISTANCE = CELL_SIZE
MAGIC_NUMBER = 42

def make2dList(rows, columns, initial):
    """Create a rows x columns 2d List initially filled with 'initial' value.

    :param rows: Number of rows in the 2d List.
    :param columns: Number of columns in the 2d List.
    :param initial: Initial value to be populated in all the cells.
    :return: 2d List of integers.
    """

    result = []
    for row in range(rows):
        result += [[initial] * columns]

    return result

def init(data):
    """ Initialize the 'struct' variables at the start.

    :param data: Data type bundling together named data items.
    :return: None
    """
    data.gameOver = False

    # Initial Highlighted Cell
    data.hRow = data.rows // 2
    data.hCol = data.cols // 2

    # Values entered in individual cells.
    data.cellValues = make2dList(data.rows, data.cols, -1)
    data.cellColors = make2dList(data.rows, data.cols, "white")

    # Current player turn.
    data.currentPlayer = 0

    # Cell UI colors
    data.highlightColor = ['lightBlue', 'orange']
    data.textColor = ['darkBlue', 'darkOrange']

    # Keep Player Score
    data.score = [0, 0]

    # Best 'Turn Sum' for each player in the round.
    data.bestScore = [0, 0]

    # Number of cells already filled up.
    data.filledCells = 0

def mousePressed(event, data):
    """ Dummy Function.

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    pass

def moveHighlightedCell(dx, dy, data):
    """ Move the highlighted cell.

    At any time, a single cell in the board is highlighted. The current player
    can change the highlighted cell with the up, down, left, and right arrows
    (with wraparound, so for example, pressing the left arrow with the selection
    in the leftmost column causes the selection to move to the rightmost column
    in the same row).

    :param dx: Displacement along the 'x' axis.
    :param dy: Displacement along the 'y' axis.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    data.hRow += dx
    data.hCol += dy

    if data.hCol < 0:
        data.hCol = data.cols - 1
    elif data.hCol > data.cols - 1:
        data.hCol = 0
    elif data.hRow < 0:
        data.hRow = data.rows - 1
    elif data.hRow > data.rows - 1:
        data.hRow = 0

def togglePlayer(data):
    """ Two players (one blue, the other orange) take turns moving. This
    function simply toggles turns between the two players.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    data.currentPlayer = 1 if data.currentPlayer == 0 else 0

def resetBoard(data):
    """ Reset the board for the next round of play.

    a) Toggle the player.
    b) Fill the board with 'empty-values'.
    c) Reposition the highlighted cell and
    d) Check if the game is over.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    togglePlayer(data)

    for row in range(data.rows):
        for column in range(data.cols):
            data.cellValues[row][column] = -1
            data.cellColors[row][column] = "white"

    data.hRow = data.rows // 2
    data.hCol = data.cols // 2
    data.bestScore = [0, 0]

    if data.score[0] >= 5 or data.score[1] >= 5:
        data.gameOver = True

def isValidLocation(data, dx, dy):
    """ Check if the new location on the board remains valid.

    :param data: 'Struct' data type bundling together named data items.
    :param dx: Displacement along the 'x-axis'.
    :param dy: Displacement along the 'y-axis'.
    :return: True if the new location is valid. False, otherwise.
    """

    if 0 <= data.hRow + dx <= data.rows - 1:
        if 0 <= data.hCol + dy <= data.cols - 1:
            return True

    return False

def turnSum(data):
    """ When a digit is placed, the players "turn sum" is the sum of all the
    digits neighboring that digit, plus the digit itself.

    :param data: 'Struct' data type bundling together named data items.
    :return: Turn Sum, an integer.
    """
    adjacentSum = 0
    directions = [(-1, -1), (-1, 0), (-1, +1),
                  (0,  -1), (0,  0), (0,  +1),
                  (+1, -1), (+1, 0), (+1, +1)]

    for (dx, dy) in directions:
        if isValidLocation(data, dx, dy):

            row = data.hRow + dx
            column = data.hCol + dy

            if data.cellValues[row][column] != -1:
                adjacentSum += data.cellValues[row][column]

    return adjacentSum

def winRound(data, player):
    """ Update the score for the player passed to the function. Each round win
    is scored at 1 point. Also, reset the board for the next round of play.

    :param data: 'Struct' data type bundling together named data items.
    :param player: Player whose score is to be updated. In case of ties, -1 will
                   be passed as the player number, in which case, 1 point is
                   equally added to each player's score.
    :return: None
    """

    if player == -1:
        data.score[0] += 1
        data.score[1] += 1
    else:
        data.score[player] += 1

    resetBoard(data)

def tieWinner(data):
    """ Determine the winner of the round when the board is full and no more
    moves are possible.

    :param data: 'Struct' data type bundling together named data items.
    :return: 0 or 1 as the player number. In case of ties, return -1
    """

    if data.bestScore[0] > data.bestScore[1]:
        return 0
    elif data.bestScore[1] > data.bestScore[0]:
        return 1
    else:
        return -1

def makeMove(data, value):
    """ Make a legal move on the board.

    To make a move, the current player can press a single digit key. If the
    current selection is empty, that digit is displayed in the currently
    selected cell, using the current player's color. Otherwise, if the current
    selection is not empty, the current player loses that round.

    :param data: 'Struct' data type bundling together named data items.
    :param value: Single Digit integer entered by the user.
    :return: None
    """

    row = data.hRow
    col = data.hCol

    # Fill cell and keep count of the cells filled up.
    data.filledCells += 1
    data.cellValues[row][col] = value
    data.cellColors[row][col] = data.textColor[data.currentPlayer]

    # Find the turnSum
    score = turnSum(data)
    if (abs(score - MAGIC_NUMBER) <
            abs(data.bestScore[data.currentPlayer] - MAGIC_NUMBER)):
        data.bestScore[data.currentPlayer] = score

    # See if the round is complete and we have a winner.
    if score == MAGIC_NUMBER:
        winRound(data, data.currentPlayer)
    elif data.filledCells == data.rows * data.cols:
        winRound(data, tieWinner(data))
    else:
        togglePlayer(data)

def keyPressed(event, data):
    """ Extract char and/or keysym from event.char and event.keysym; modify data
    based on key pressed.

    Pressing the ArrowKeys 'Left', 'Right' and 'Down' call the function
    moveHighlightedCell to move the highlighted cell one place in the direction
    specified by the arrow key.

    :param event: Key Press event captured.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if not data.gameOver:
        row = data.hRow
        col = data.hCol

        if event.keysym.isdigit():
            if data.cellValues[row][col] == -1:
                makeMove(data, int(event.keysym))
            else:
                togglePlayer(data)
                winRound(data, data.currentPlayer)

        elif event.keysym == "Left":
            moveHighlightedCell(0, -1, data)
        elif event.keysym == "Right":
            moveHighlightedCell(0, +1, data)
        elif event.keysym == "Up":
            moveHighlightedCell(-1, 0, data)
        elif event.keysym == "Down":
            moveHighlightedCell(+1, 0, data)

def timerFired(data):
    """ Dummy Function.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    pass

def getCellBounds(row, column, data):
    """Determine the bounds of the cell to be drawn.

    :param row: Row number of the cell.
    :param column: Column number of the cell.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    x0 = GRID_MARGIN
    y0 = 2 * GRID_MARGIN

    rowHeight = (data.height - (2 * GRID_MARGIN) - GRID_MARGIN) / data.rows
    colWidth = (data.width - (2 * GRID_MARGIN)) / data.cols

    xn = x0 + column * colWidth
    yn = y0 + row * rowHeight

    return xn, yn, (xn + colWidth), (yn + rowHeight)

def drawCell(canvas, x0, y0, xn, yn, value, backgroundColor, textColor):
    """Draw a rectangular cell on the Board.

    :param x0: x-coordinate of the top-left corner of the cell.
    :param y0: y-coordinate of the top-left corner of the cell.
    :param xn: x-coordinate of the bottom-right corner of the cell.
    :param yn: y-coordinate of the bottom-right corner of the cell.
    :param value: Value to be displayed in the cell.
    :param backgroundColor: Background color of the cell.
    :param textColor: Color of the text displayed in the cell.
    :return: None
    """

    canvas.create_rectangle(x0, y0, xn, yn, fill=backgroundColor, width=2)

    if value > -1:
        canvas.create_text((x0 + xn) / 2, (y0 + yn) / 2,
                           text=value,
                           fill=textColor,
                           font="arial 12 bold")

def drawBoard(canvas, data):
    """Draw the 42 board.

    To draw the board, we simply iterate over every cell (with two variables
    running over every row and column), and repeatedly call the drawCell
    function.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    for row in range(data.rows):
        for column in range(data.cols):
            (x0, y0, xn, yn) = getCellBounds(row, column, data)

            textColor = data.cellColors[row][column]

            if row == data.hRow and column == data.hCol:
                highlightColor = data.highlightColor[data.currentPlayer]
            else:
                highlightColor = "white"

            drawCell(canvas, x0, y0, xn, yn,
                     data.cellValues[row][column],
                     highlightColor,
                     textColor)

def drawScoreCard(canvas, data):
    """ Display the current score at the top of the baord.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    spaceWidth = (data.width - (2 * GRID_MARGIN) - SCORE_DISTANCE) / 2

    canvas.create_text(GRID_MARGIN + spaceWidth,
                       GRID_MARGIN,
                       text=data.score[0],
                       fill=data.textColor[0],
                       font="arial " + str(int((2 / 5) * CELL_SIZE)) + " bold")

    canvas.create_text(GRID_MARGIN + spaceWidth + SCORE_DISTANCE,
                       GRID_MARGIN,
                       text=data.score[1],
                       fill=data.textColor[1],
                       font="arial " + str(int((2 / 5) * CELL_SIZE)) + " bold")

def drawGameOver(canvas, data):
    """ Display the "Game Over!" message at the end of play.

    When the game is over, the message "Game Over" is displayed, and the score
    and all further keypresses should are ignored.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.gameOver:
        canvas.create_text(data.width / 2,
                           data.height / 2,
                           text="Game Over!",
                           font="arial 35 bold",
                           fill="green")

def redrawAll(canvas, data):
    """ Redraw all canvas elements from back to front based on values in data.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    drawBoard(canvas, data)
    drawScoreCard(canvas, data)
    drawGameOver(canvas, data)

def run(rows, columns):
    """ Creates canvas and data; registers event handlers; calls init; starts
    timer; etc.

    :param rows: Number of rows in the grid
    :param columns: Number of columns in the grid
    :param margin: Margin size around the grid.
    :param cellSize: Cell size in the grid.
    :return: None
    """
    # Note that the wrapper functions are defined INSIDE The run function!

    def redrawAllWrapper(canvas, data):
        # Every canvas item is an object that tkinter keeps track of. To clear
        # the canvas, use the delete method. Give it the special paramter "ALL"
        # to delete all items on the canvas.
        # https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        # http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.delete-method

        canvas.delete(ALL)
        canvas.create_rectangle(0, 0,
                                data.width, data.height,
                                fill="white",
                                width=0)
        redrawAll(canvas, data)

        # This command is used to bring the application "up to date" by entering
        # the event loop repeated until all pending events (including idle
        # callbacks) have been processed.
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)

        # Tkinter root windows have a method called "after" which can be used to
        # scheduled a function to be called after a given period of time. If
        # that function itself calls "after", you've set up an automatically
        # recurring event.
        # Bear in mind that "after" does not guarantee the function will run
        # exactly on time. It only /schedules/ the job to be run  after a given
        # amount of time. If the app is busy there may be a delay before it is
        # called since tkinter is single-threaded. The delay is typically in
        # microseconds.
        # https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Sometimes, it is useful to have a data type similar to C 'struct',
    # bundling together named data items. An empty class definition will
    # do nicely.
    # https://stackoverflow.com/questions/1878710/struct-objects-in-python/1878775#1878775
    class Struct(object):
        pass

    data = Struct()
    data.rows = rows
    data.cols = columns
    data.width = (2 * GRID_MARGIN) + (columns * CELL_SIZE)
    data.height = (2 * GRID_MARGIN) + (rows * CELL_SIZE) + GRID_MARGIN
    data.timerDelay = 250 #milliseconds

    # Setup the initial status of the canvas
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    #Set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))

    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    timerFiredWrapper(canvas, data)

    # and launch the app
    root.mainloop()  # blocks until window is closed

def playGame42(rows, cols):
    run(rows, cols)

playGame42(5, 5)
