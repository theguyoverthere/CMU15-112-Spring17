#******************************************************************************#
# Author: Tarique Anwer
# Date:   10/6/2017
# Description: Write Tetris according to the design given in this step-by-step
#              tutorial using our event-based animation framework (starting with
#              events-example0.py). You may not use a different design, even if
#              you think there's a better way to do it (there probably is, but
#              you still have to do it this way). This may seem limiting, but
#              sometimes you are given specs at Polya Step 1 (just indicating
#              the problem to solve), and other times at Polya Step 2 (also
#              indicating the algorithms to use). This is one of those second
#              kind of specs. Your task is to do Polya Step 3, and write the
#              corresponding code, and then using this week's event animation
#              framework.
#              http://www.kosbie.net/cmu/spring-17/15-112/notes/notes-tetris/
#              TetrisForIntroIntermediateProgrammers.html
#
#              Design Overview:
#              1. Our design includes two main elements:  a board and a falling
#                 piece.  In the picture, the board contains all blue (empty)
#                 cells except in the bottom three rows, where it contains
#                 various other colors.  The falling piece is the red piece in
#                 the picture.  In our design, this is not part of the board,
#                 but is drawn over the board.
#
#              2. More specifically, the board is a 2-dimensional list of color
#                 names (strings like "red", "blue", "green").  Initially, the
#                 board is full of one color, the emptyColor ("blue" in our
#                 sample code).  As falling pieces are transferred onto the
#                 board, other colors are introduced.
#
#              3. The goal of the game is to fill rows entirely with non-empty
#                 colors.
#
#              4. The falling piece is a 2-dimensional list of booleans,
#                 indicating whether the given cell is or is not painted in this
#                 piece.  For example, here is the definition of an S piece:
#                 sPiece = [
#                          [ False, True, True ],
#                          [ True,  True, False ]
#                          ]
#              5. As noted, the falling piece is not part of the board, but
#                 drawn over the board.  It becomes part of the board when it
#                 can no longer fall and we place it on the board, which will
#                 not happen until several steps from now in our design process.
#
#              6. The game is graphical and event-based.  This is achieved by
#                 using Tkinter as we have in previous animations..
#
#              7. Important debugging hint: you almost surely will want to add
#                 pausing (say, with "p"), unpausing (also with "p", or maybe
#                 "g" for "go"), stepping while pausing (with "s"),
#                 and resetting / calling init() again (say with "r"). These can
#                 be invaluable when trying to debug animations.
#
#******************************************************************************#
from tkinter import *
import random
import copy

def init(data):
    """Initialize the 'struct' variables at the start.

    :param data: Data type bundling together named data items.
    :return: None
    """

    data.emptyColor = "gray"
    data.board = [([data.emptyColor] * data.cols) for row in range(data.rows)]
    data.score = 0

    # Standard Piece definitions.Each piece is symmetrically defined in order to
    # make the rotation of pieces easier. In this design, the falling piece is
    # represented by a 2-dimensional list of booleans, indicating whether the
    # given cell is or is not painted in this piece.  (note that they are
    # provided in their standard configurations -- how they should enter the
    # board from the top -- so, for example, the T piece is upside down)

    oPiece = [[1, 1],
              [1, 1]]

    jPiece = [[1, 0, 0],
              [1, 1, 1],
              [0, 0, 0]]

    lPiece = [[0, 0, 1],
              [1, 1, 1],
              [0, 0 ,0]]

    sPiece = [[0, 1, 1],
              [1, 1, 0],
              [0, 0, 0]]

    tPiece = [[0, 1, 0],
              [1, 1, 1],
              [0, 0, 0]]

    zPiece = [[1, 1, 0],
              [0, 1, 1],
              [0, 0, 0]]

    iPiece = [[0, 0, 0, 0],
              [1, 1, 1, 1],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    tetrisPieceColors = ["medium violet red", "dodger blue", "orange",
                         "gold", "yellow green", "dark violet", "purple"]

    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors

    # Falling Piece
    newFallingPiece(data)
    data.gameOver = False

def isRowFull(data, row):
    """ Check if the current row is full.

    The function iterates through all the cells in the row to see if there is
    any cell with the same color as data.emptyColor. If so, the function returns
    False immediately. If all the cells are 'colored' however, the function
    returns True.

    :param data: 'Struct' data type bundling together named data items.
    :param row: Row number to be removed.
    :return: None
    """

    (rows, columns) = len(data.board), len(data.board[0])

    for column in range(columns):
        if data.board[row][column] == data.emptyColor:
            return False

    return True

def removeFullRows(canvas, data):
    """Remove all full rows from the board.

    This function will iterate a variable, oldRow, from the bottom to the top of
    the board (that is, from rows-1 to 0).  It will also start another variable,
    newRow, at the bottom of the board.  Each oldRow that is not full is copied
    to the newRow, which is then decremented by one.  Each oldRow that is full
    is not copied, and the fullRows counter is incremented. At the end, the rows
    on top are cleared (set to emptyColor) as necessary

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: Number of rows removed
    """

    (rows, columns) = len(data.board), len(data.board[0])
    newRow = rows - 1
    fullRows = 0

    for oldRow in range(rows - 1, -1, -1):
        if isRowFull(data, oldRow):
            fullRows += 1
        else:
            for column in range(columns):
                data.board[newRow][column] = data.board[oldRow][column]
            newRow -= 1

    data.score += fullRows ** 2

def newFallingPiece(data):
    """Generate a new tetromino piece.

    The newFallingPiece function is responsible for randomly choosing a new
    piece, setting its color, and positioning it in the middle of the top row.
    The first step is to randomly choose an index from the tetrisPieces list ,
    then to set the data values holding the fallingPiece and the
    fallingPieceColor to the respective elements from the lists of tetrisPieces
    and tetrisPieceColors.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    element = random.randint(0, len(data.tetrisPieces) - 1)

    data.fallingPiece = data.tetrisPieces[element]
    data.fallingPieceColor = data.tetrisPieceColors[element]

    data.fallingPieceRows = len(data.fallingPiece)    #Height of the piece
    data.fallingPieceCols = len(data.fallingPiece[0]) #Width of the piece

    #Left-Top Coordinate of the Falling Piece
    data.fallingPieceRow = 0
    data.fallingPieceCol = (data.cols // 2) - (data.fallingPieceCols // 2)

def keyPressed(event, data):
    """ Extract char and/or keysym from event.char and event.keysym; modify data
    based on key pressed.

    Pressing the ArrowKeys 'Left', 'Right' and 'Down' call the function
    moveFallingPiece to move the falling tetromino piece in that direction.
    Pressing the 'Up' arrow key, rotates the tetromino piece using the
    rotateFallingPiece function.

    Pressing 'r' allows the user to restart the game, once it is over.

    :param event: Key Press event captured.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.gameOver:
        if event.keysym == "r":
            init(data)
    else:
        if event.keysym == "Up":
            rotateFallingPiece(data)
        elif event.keysym == 'Left':
            moveFallingPiece(data, 0, -1)
        elif event.keysym == 'Right':
            moveFallingPiece(data, 0, +1)
        elif event.keysym == 'Down':
            moveFallingPiece(data, +1, 0)


def placeFallingPiece(data):
    """ Place the falling piece on the board.

    This function is quite similar to drawFallingPiece, only rather than draw
    the cells, we load the corresponding positions on the board with the
    fallingPieceColor.  In this way, the piece is placed on the board.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    (rows , columns) = len(data.fallingPiece), len(data.fallingPiece[0])

    for row in range(rows):
        for column in range(columns):
            if data.fallingPiece[row][column] > 0:
                bRow = row + data.fallingPieceRow
                bCol = column + data.fallingPieceCol

                data.board[bRow][bCol] = data.fallingPieceColor

def drawScore(canvas, data):
    """Display Score at the end of the game.

     In the removeFullRows function, we increment the score by the square of
     total number of full rows removed in order to reward removing multiple
     lines at once.

     Now that we have the score, we display the score using the drawScore
     function.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    canvas.create_text(data.width / 2, data.height / 2 + 40,
                       text="Score: " + str(data.score),
                       font="Arial 20 bold",
                       fill="orange")

def drawGameOver(canvas, data):
    """ Draw the End of the game.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.gameOver:
        # Fill the background and draw the board.
        canvas.create_rectangle(0, 0,
                                data.width + 1, data.height + 1,
                                fill="white",
                                width=0)

        canvas.create_text(data.width/2, data.height/2,
                           text="Game over!",
                           font="Arial 26 bold",
                           fill="orange")

        drawScore(canvas, data)

def timerFired(data):
    """ Modify data based on elapsed time.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if not moveFallingPiece(data, +1, 0):
        placeFallingPiece(data)

        if not data.gameOver:
            newFallingPiece(data)

            if not fallingPieceIsLegal(data):
                data.gameOver = True

def mousePressed(event, data):
    """ Extract mouse location via event.x, event.y; modify data based on mouse
    press location

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    pass

def make2dList(rows, columns):
    """Create a Two Dimensional List

    :param rows: Number of rows in the 2d List
    :param columns: Number of columns in the 2d List
    :return: Two Dimensional List
    """
    result = []
    for row in range(rows):
        result += [[0] * columns]

    return result

def rotateMatrixCounterClockwise(matrix):
    """Rotate a 2d List Counter Clockwise 90 degree.

    :param matrix: Two Dimensional List
    :return: Rotated 2d List
    """

    (rows, columns) = (len(matrix), len(matrix[0]))
    result = make2dList(columns, rows)

    for column in range(columns - 1, -1, -1):
        for row in range(rows):
            result[columns - column - 1][row] = matrix[row][column]

    return result

def rotateFallingPiece(data):
    """Rotate the falling piece.

    We start by storing the old piece (the 2d list of booleans), its location,
    and its dimensions in local variables (because we may need these to undo our
    move if it turns out to be illegal).  Next, we compute the new dimensions,
    by reversing the old dimensions.

    Next, we compute the new location. Our goal is to keep the center of the
    falling piece constant (or, given that this is not possible if we have an
    even number of rows or columns, to keep the center as constant as possible).

    To make this happen, we observe that the center row of the falling piece can
    be computed as the sum of its top row plus half its height in rows. That is:
           centerRow = fallingPieceRow + fallingPieceRows/2
    Now, we actually have two pieces -- the old falling piece, before the
    rotation, and the new falling piece, after the rotation. We can compute each
    of their centers as such:
           oldCenter = oldRow + oldRows/2    newCenter = newRow + newRows/2
    To keep the old and new centers the same, we just set oldCenter equal to
    newCenter in the equations above.

    Finally, we check if this rotation makes the falling piece go off the board
    or collide with a non-empty cell on the board (simply reusing our code from
    the previous steps, where we wrote a function that tests if the current
    board is legal or not), and if either of these conditions occurs, we restore
    the piece, its location, and its dimensions to their original values.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    oldFallingPiece = copy.deepcopy(data.fallingPiece)
    newFallingPiece = rotateMatrixCounterClockwise(oldFallingPiece)

    # Dimensions of the falling piece
    oldRows = data.fallingPieceRows  # Height of the piece
    oldCols = data.fallingPieceCols # Width of the piece

    newRows = oldCols
    newCols = oldRows

    # Original Top-Left coordinates of the falling piece
    oldRow = data.fallingPieceRow
    oldCol = data.fallingPieceCol

    # New Top-Left coordinates of the falling piece
    newRow = oldRow + (oldRows - newRows) / 2
    newCol = oldCol + (oldCols - newCols) / 2

    # Update the piece
    data.fallingPiece = newFallingPiece
    data.fallingPieceRow = int(newRow)
    data.fallingPieceCol = int(newCol)
    data.fallingPieceRows = newRows
    data.fallingPieceCols = newCols

    # If the move was illegal, revert the change
    if not fallingPieceIsLegal(data):
        data.fallingPiece = oldFallingPiece

        data.fallingPieceRow = oldRow
        data.fallingPieceCol = oldCol

        data.fallingPieceRows = oldRows
        data.fallingPieceCols = oldCols

def fallingPieceIsLegal(data):
    """Check if the falling piece of tetromino is legal.

    We only want to move in a given direction if it is legal to do so.  There
    are two reasons why it may not be legal:  the falling piece may wind up off
    of the board, or a part of the falling piece may collide with a non-empty
    cell on the board.  In either case, we should not move the falling piece.

    The function iterates over every cell (every row and every column) in the
    fallingPiece, and for those cells which are part of the falling piece
    (that is, where the falling piece list has a True value), rather than draw
    the cell (as drawFallingPiece does), this method confirms that:
    (1) the cell is in fact on the board; and
    (2) the color at that location on the board is the emptyColor.  If either of
        these checks fails, the function immediately returns False.

    If all the checks succeed for every cell in the fallingPiece, the function
    returns True.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    (rows , columns) = len(data.fallingPiece), len(data.fallingPiece[0])

    for row in range(rows):
        for column in range(columns):
            if data.fallingPiece[row][column] > 0:
                (x0, y0, xn, yn) = getCellBounds(data.fallingPieceRow + row,
                                                 data.fallingPieceCol + column,
                                                 data)

                if ((x0 < data.margin) or
                    (xn > data.width - data.margin) or
                    (y0 < data.margin) or
                    (yn > data.height -data.margin)):
                    return False

                bRow = data.fallingPieceRow + row
                bCol = data.fallingPieceCol + column

                if data.board[bRow][bCol] != data.emptyColor:
                    return False

    return True

def moveFallingPiece(data, dRow, dCol):
    """ Move the tetromino by dRow and dCol cells.

    We use "dRow" to signify a change in rows. Similarly, "dCol" is the
    change in columns. With this function, we can move to the left by calling
    moveFallingPiece(data,0,-1).  Similarly, we can move to the right with
    moveFallingPiece(data,0,+1).  And to move down, we hold our column constant
    and add one to our row:  moveFallingPiece(data,+1,0).

    First, we simply make the move by modifying the data values storing the
    location of the left-top corner of the falling piece.  Next, we test if this
    new location of the falling piece is legal. If the new location is not legal
    (because it was off the board or because it collided with a non-empty cell
    on the board), then we undo the move we just made, by resetting the data
    values to their original values prior to the call to moveFallingPiece.

    :param data: 'Struct' data type bundling together named data items.
    :param dRow: Displacement in terms of rows.
    :param dCol: Displacement in terms of columns.
    :return: None
    """
    data.fallingPieceRow += dRow
    data.fallingPieceCol += dCol

    if not fallingPieceIsLegal(data):
        data.fallingPieceRow -= dRow
        data.fallingPieceCol -= dCol

        return False

    return True

def drawFallingPiece(canvas, data):
    """ Draw the falling piece of tetromino.

    After calling drawBoard, drawFallingPiece is called, so the falling piece is
    drawn over the board (in this way, to the user it looks like the falling
    piece is on the board, but in reality it is stored separately and drawn
    separately).  To draw the falling piece, we iterate over each cell in the
    fallingPiece, and if the value of that cell is True, then we should draw it
    reusing the same drawCell function that drawBoard uses, but in the color of
    the fallingPiece (rather than the color stored in the board for that row and
    column). However, we have to add the offset of the left-top row and column
    (that is, fallingPieceRow and fallingPieceCol) so that the fallingPiece is
    properly positioned on the board.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    (rows , columns) = len(data.fallingPiece), len(data.fallingPiece[0])

    for row in range(rows):
        for column in range(columns):
            if data.fallingPiece[row][column] > 0:
                (x0, y0, xn, yn) = getCellBounds(data.fallingPieceRow + row,
                                                 data.fallingPieceCol + column,
                                                 data)
                drawCell(canvas, x0, y0, xn, yn, color=data.fallingPieceColor)

def getCellBounds(row, column, data):
    """Determine the bounds of the cell to be drawn.

    :param row: Row number of the cell.
    :param column: Column number of the cell.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    x0 = data.margin
    y0 = data.margin

    rowHeight = (data.height - (2 * data.margin)) / data.rows
    colWidth = (data.width - (2 * data.margin)) / data.cols

    xn = x0 + column * colWidth
    yn = y0 + row * rowHeight

    return xn, yn, (xn + colWidth), (yn + rowHeight)

def drawCell(canvas, x0, y0, xn, yn, color):
    """Draw a rectangular cell on the Tetris Board.

    To draw a cell a given color, we simply draw a rectangle with a wide outline
    which is 25% the cell width in this case.

    :param canvas: Canvas, on which the grid is displayed.
    :param x0: x-coordinate of the top-left corner of the cell.
    :param y0: y-coordinate of the top-left corner of the cell.
    :param xn: x-coordinate of the bottom-right corner of the cell.
    :param yn: y-coordinate of the bottom-right corner of the cell.
    :param color: Color of the cell.
    :return: None
    """
    canvas.create_rectangle(x0, y0, xn, yn, fill=color,width=5)

def drawBoard(canvas, data):
    """Draw the Tetris board.

    To draw the board, we simply iterate over every cell (with two variables
    running over every row and column), and repeatedly call the drawCell
    function. The drawCell function draws a given cell using the color stored in
    the board list corresponding to that cell (that is, in board[row][col]).

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    for row in range(data.rows):
        for column in range(data.cols):
            (x0, y0, xn, yn) = getCellBounds(row, column, data)
            drawCell(canvas, x0, y0, xn, yn, color=data.board[row][column])

def drawGame(canvas, data):
    """Fill the background and draw the Tetris board.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    canvas.create_rectangle(0, 0, data.width, data.height, fill="orange")

    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)

def redrawAll(canvas, data):
    """ Redraw all canvas elements from back to front based on values in data.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    rowsRemoved = 0

    drawGame(canvas, data)
    removeFullRows(canvas, data)
    drawGameOver(canvas, data)

def run(rows, columns, margin, cellSize):
    """ Creates canvas and data; registers event handlers; calls init; starts
    timer; etc.

    :param rows: Number of rows in the Tetris grid
    :param columns: Number of columns in the Tetris grid
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
                                width = 0)
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
    data.margin = margin
    data.width = (2 * margin) + (columns * cellSize)
    data.height = (2 * margin) + (rows * cellSize)
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


####################################
# playTetris() [calls run()]
####################################

def playTetris():
    """Play Tetris!

    :return: None
    """
    rows = 25
    cols = 15
    margin = 20 # margin around grid
    cellSize = 30 # width and height of each cell

    run(rows, cols, margin, cellSize)

playTetris()
