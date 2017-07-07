#******************************************************************************#
# Author: Tarique Anwer
# Date:   1/7/2017
# Description: Mimic the Game like application in the associated video!
#******************************************************************************#
from tkinter import *

MIN_FONT_SIZE = 10
MAX_FONT_SIZE = 60
HEIGHT_OFFSET = 10
WIDTH_OFFSET  = 10
GRID_ROWS     = 10
GRID_COLUMNS  = 10
GRID_MARGIN   =  0
CIRCLE_RADIUS =  5
CLOCK_WIDTH   = 10
CLOCK_HEIGHT  =  5
PLAY_TIME     = 20
SCREEN_REFRESH_INTERVAL       = 50
HELP_SCREEN_FIXED_FONT_SIZE   = 12
SPLASH_SCREEN_FIXED_FONT_SIZE = 20
GAME_OVER_FIXED_FONT_SIZE     = 26

def init(data):
    """Initialize the 'struct' variables at the start.

    :param data: Data type bundling together named data items.
    :return: None
    """

    #Initial Mode
    data.mode = "splashScreen"
    data.prevMode = None

    # Scrolling text on the Help Screen
    data.fontColor = None
    data.fontSize = MIN_FONT_SIZE
    data.scrollingRight = True
    data.hx = data.width / 2

    # 'Scores' under each cell.
    data.board = []
    for row in range(GRID_ROWS):
        data.board += [[0] * GRID_COLUMNS]

    # Timer display on the Play Game Screen
    data.count = 0
    data.playTime = PLAY_TIME

    # Coordinates of the top left corner of the full board.
    data.x0 = GRID_MARGIN - data.width
    data.y0 = GRID_MARGIN - data.height

    # Current cell at the center of the screen
    data.currentRow, data.currentCol = getCurrentLocation(data,
                                                          data.width / 2,
                                                          data.height / 2)

    # Displacement due to an arrow key press
    data.dx = 0
    data.dy = 0
#------------------------------------------#
#           Splash Screen Mode             #
#------------------------------------------#
def splashScreenMousePressed(event, data):
    """ Dummy Function.

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    pass

def splashScreenKeyPressed(event, data):
    """ Extract char and/or keysym from event.char and event.keysym; modify data
    based on key pressed.

    Pressing 'h' displays the 'Help Screen'
    Pressing 'p' starts the 'Game'

    :param event: Key Press event captured.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if event.keysym == "h":
        data.mode = "help"
        data.prevMode = "splashScreen"
    elif event.keysym == "p":
        data.mode = "playGame"

def splashScreenTimerFired(data):
    """ Modify data on the Splash Screen based on elapsed time.

    The Splash Screen is displayed with the visual effect of the text 'coming
    out' of the window and then restarting all over again.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.fontSize < MAX_FONT_SIZE:
        data.fontSize += 2
    else:
        data.fontSize = MIN_FONT_SIZE

def splashScreenRedrawAll(canvas, data):
    """ Redraw all Splash Screen canvas elements from back to front based on
    values in data.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    canvas.create_text(data.width / 2,
                      (data.height / 2 - HEIGHT_OFFSET),
                       font="Arial " + str(data.fontSize) + " bold",
                       text="The Hw6 Game-Like App!")

    canvas.create_text(data.width / 2,
                      (data.height / 2) +
                      (MAX_FONT_SIZE - MIN_FONT_SIZE),
                       font="Arial " + str(SPLASH_SCREEN_FIXED_FONT_SIZE),
                       text="Press 'p' to play, 'h' for help!")

#------------------------------------------#
#              Play Game Mode              #
#------------------------------------------#
def centerSelectedCell(xm, ym,data):
    """ Center the selected location.

    The point at which the mouse click occurs is moved to the center of the
    screen and the screen redrawn-again.

    :param xm: x-coordinate of the Mouse Click
    :param ym: y-coordinate of the Mouse Click
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    # Offset of the mouse click from the center of the screen.
    dx = xm - data.width  / 2
    dy = ym - data.height / 2

    # Update the position of the top-left corner of the grid.
    data.x0 -= dx
    data.y0 -= dy

def playGameMousePressed(event, data):
    """  Center the selected location.

    When the Mouse is pressed during the "Play Game" Mode, the screen is
    centered to the cell in which the mouse click occurred. Also, the count in
    the cell goes up by 1.

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    centerSelectedCell(event.x, event.y, data)

def moveBoard(dx, dy, data):
    """ Update the location of the board with the displacement dx, dy.
    The circle at the center of the screen remains constant and does not move.
    The entire board however can be scrolled and moved using the arrow keys on
    the keyboard.

    It is also possible scroll outside the boundaries of the board, in which
    case the board is partially,completely or not displayed on the screen at
    all.

    :param dx: Displacement along the x axis.
    :param dy: Displacement along the y axis.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    data.dx = dx
    data.dy = dy

    data.x0 += data.dx
    data.y0 += data.dy

def playGameKeyPressed(event, data):
    """ Extract char and/or keysym from event.char and event.keysym; modify data
    based on key pressed.

    Pressing keys have the following effects:

    'h'     - displays the 'Help Screen'.
    'space' - resets the timer on the screen.
    'Tab'   - Helps you win game. Please don't abuse ;)
    'Left'  - The Left arrow key,  scrolls the grid 10 pixels to the left.
    'Right' - The Left arrow key,  scrolls the grid 10 pixels to the right.
    'Up'    - The Left arrow key,  scrolls the grid 10 pixels up.
    'Down'  - The Left arrow key,  scrolls the grid 10 pixels down.

    :param event: Key Press event captured.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if event.keysym == "h":
        data.mode = "help"
        data.prevMode = "playGame"
    elif event.keysym == "space":
        data.playTime = PLAY_TIME
    elif event.keysym == "Tab":
        data.mode = "winGame"
    elif event.keysym == "Left":
        moveBoard(+10, 0, data)
    elif event.keysym == "Right":
        moveBoard(-10, 0, data)
    elif event.keysym == "Up":
        moveBoard(0, +10, data)
    elif event.keysym == "Down":
        moveBoard(0, -10, data)

def resetBoard(data):
    """ Reset the 'Struct' values so that the game can be started again.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    data.prevMode = None

    data.x0 = GRID_MARGIN - data.width
    data.y0 = GRID_MARGIN - data.height

    for row in range(GRID_ROWS):
        for column in range(GRID_COLUMNS):
            data.board[row][column] = 0

    data.currentRow, data.currentCol = getCurrentLocation(data,
                                                          data.width / 2,
                                                          data.height / 2)
    data.playTime = PLAY_TIME

def playGameTimerFired(data):
    """ Modify data on the Splash Screen based on elapsed time.

    Approximate time by looping through a counter, so that an approximation of
    a clock is displayed on the screen. The screen refreshes every 50 ms, hence
    loop 20 times to approximate a complete second.

    This 'time-counter' does NOT closely approximate time and a better solution
    may be required for more accuracy.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    data.count += 50
    if data.count == 1000:
        data.count = 50
        data.playTime -= 1

        if data.playTime <= 0:
            resetBoard(data)
            data.mode = "gameOver"

def getCellBounds(row, column, data):
    """ Determine the bounds of the cell to be drawn.

    :param row: Row number of the cell.
    :param column: Column number of the cell.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    x0 = data.x0 + data.dx
    y0 = data.y0 + data.dy

    rowHeight = (data.height - (2 * GRID_MARGIN))/ (GRID_ROWS / 2)
    colWidth = (data.width - (2 * GRID_MARGIN)) / (GRID_COLUMNS / 2)

    xn = x0 + column * colWidth
    yn = y0 + row * rowHeight

    data.dx = 0
    data.dy = 0

    return xn, yn, (xn + colWidth), (yn + rowHeight)

def drawCell(canvas, data, row, column, x0, y0, xn, yn, color):
    """ Draw a rectangular cell on the Board.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :param row: Row in the board.
    :param column: Column in the board.
    :param x0: x-coordinate of the top-left corner of the cell.
    :param y0: y-coordinate of the top-left corner of the cell.
    :param xn: x-coordinate of the bottom-right corner of the cell.
    :param yn: y-coordinate of the bottom-right corner of the cell.
    :param color: Color of the cell.
    :return: None
    """

    # Draw the rectangular cell.
    canvas.create_rectangle(x0, y0,
                            xn, yn,
                            fill=color,width=2)

    # Add the rectangular coordinates of the cell.
    canvas.create_text((x0 + xn) / 2, y0 + (yn - y0) / 3,
                       text="(" + str(row) + ", " + str(column) + ")")

    # Add the 'score' of each cell, so to say. This is simply the number of
    # times the cell has been selected or positioned at the center of the
    # displayed screen.
    canvas.create_text((x0 + xn) / 2,    y0 + ((2 * (yn - y0)) / 3),
                       text=data.board[row][column])

def drawBoard(canvas, data):
    """ Draw the Game Board on the screen, the bottom right quarter of which is
    displayed on the screen at the start of the play. The cells are filled with
    alternating colors or "light yellow" and "light blue". The one at the
    center of the screen is highlighted by painting it "gold" or "blue".

    In the design below, even numbered cells are filled with "light yellow",
    and odd numbered cells with "light blue".

    Each cell has its coordinates displayed on the screen, along with a 'score',
    so to say which is essentially the number of times, the cell was selected
    by a mouse click or positioned at the center of the screen by scrolling
    the board appropriately.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    for row in range(GRID_ROWS):
        for column in range(GRID_COLUMNS):
            (x0, y0, xn, yn) = getCellBounds(row, column, data)

            color = "yellow" if (row + column) % 2 == 0 else "blue"
            if (data.currentRow != row) or (data.currentCol != column):
                color = "light " + color

            drawCell(canvas, data, row, column, x0, y0, xn, yn, color=color)

def drawClock(canvas, data):
    """ Draw the clock at the upper left corner of the board.
    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    rowHeight = (data.height - (2 * GRID_MARGIN)) / (GRID_ROWS / 2)
    colWidth = (data.width - (2 * GRID_MARGIN)) / (GRID_COLUMNS / 2)

    if data.playTime   > 10: fillColor = "gray"
    elif data.playTime >  5: fillColor = "gold"
    else: fillColor = "red"

    # The exact specifications for the clock are not present in the problem. It
    # has been drawn to visually match the clock in the problem video.

    canvas.create_rectangle(0, 0,
                            colWidth * 5 / 4, rowHeight / 3,
                            fill=fillColor)

    canvas.create_text(colWidth * 3 / 10, rowHeight / 6,
                       font="Arial 10",
                       text=str(data.playTime))

    canvas.create_text(colWidth * 3 / 4, rowHeight / 6,
                       font="Arial 10",
                       text="seconds")

def drawCircle(canvas, data):
    """Draw the circle at the center of the screen. The circle is filled with
    the color "deep pink".

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    canvas.create_oval(data.width  / 2 - CIRCLE_RADIUS,
                       data.height / 2 - CIRCLE_RADIUS,
                       data.width  / 2 + CIRCLE_RADIUS,
                       data.height / 2 + CIRCLE_RADIUS,
                       fill="deep pink")

def drawInstructions(canvas, data):
    """Draw the instructions on the screen.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    instruction = "Press 'h' for help! Use Space, Tab, MouseButton Arrows!"
    canvas.create_text(data. width * 0.5, data.height * 0.97,
                       text=instruction,
                       fill="dark blue")

def getCurrentLocation(data, xn, yn):
    """ Get the (x, y) coordinates of the current cell, given any point inside
    the cell.

    :param data: 'Struct' data type bundling together named data items.
    :param xn: x-coordinate of the point inside the cell.
    :param yn: y-coordinate of the same point inside the cell.
    :return: (row, column) coordinates of the cell.
    """
    rowHeight = (data.height - (2 * GRID_MARGIN)) / (GRID_ROWS / 2)
    colWidth = (data.width - (2 * GRID_MARGIN)) / (GRID_COLUMNS / 2)

    # See, how far it is from the top-left corner of the grid.
    deltaX, deltaY = getCurrentOffset(data, xn, yn)

    # Use the displacement vector to identify the row, column coordinates.
    row = int(deltaY // rowHeight)
    column = int(deltaX // colWidth)

    return row, column

def getCurrentOffset(data, xn, yn):
    """ Returns the distance of the cell represented by (xn, yn) from the
    top-left corner of the cell (data.x0, data.y0).

    :param data: 'Struct' data type bundling together named data items.
    :param xn: x-coordinate of the top-left corner of the cell.
    :param yn: y-coordinate of the top-left corner of the cell.
    :return: None
    """

    dx0 = xn - data.x0
    dy0 = yn - data.y0

    return dx0, dy0

def isLocationWithinBounds(data, dx0, dy0):
    """ Check if the location of the center of the screen is within the confines
    of the board. This is done by looking up the displacement vector obtained
    earlier, to see if it is lies within the board.

    :param data: 'Struct' data type bundling together named data items.
    :param dx0: Distance of the x coordinate of the cell from the x coordinate
                of the top-left corner of the board.
    :param dy0: Distance of the y coordinate of the cell from the y coordinate
                of the top-left corner of the board.
    :return: True if the center of the screen is within the boundaries of the
             board. False otherwise.
    """

    if dx0 > 0 and dy0 > 0:
        if dx0 < (2 * data.width) and dy0 < (2 * data.height):
            return True

    return False

def detectOverlap(data):
    """ Update the 'score' of a cell if it has been positioned at the center of
    the screen. Scrolling while staying centered in the same cell, does not
    update the score.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    xc = data.width / 2
    yc = data.height / 2

    # Get the (row, column) position of the cell positioned at the center of the
    # screen.
    row, column = getCurrentLocation(data, xc, yc)

    # See, how far it is from the top-left corner of the grid.
    deltaX, deltaY = getCurrentOffset(data, xc, yc)

    # Use the displacement to identify if we are still within the boundaries of
    # the board. If it is so, and the current cell is not the previous cell at
    # the center of the screen, update the score.

    if isLocationWithinBounds(data, deltaX, deltaY):
        if (data.currentRow != row) or (data.currentCol != column):

            data.board[row][column] += 1
            data.currentRow = row
            data.currentCol = column

def playGameRedrawAll(canvas, data):
    """ Redraw all canvas elements in the PlayGame mode from back to front based
    on values in data.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    drawBoard(canvas, data)
    drawClock(canvas, data)
    drawCircle(canvas, data)
    drawInstructions(canvas, data)
    detectOverlap(data)

#------------------------------------------#
#              Help Mode                   #
#------------------------------------------#
def helpMousePressed(event, data):
    """ If a Mouse click is detected, revert to the previous mode.

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    data.mode = data.prevMode

def helpKeyPressed(event, data):
    """ Dummy function.

    :param event: A Key Press Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    pass

def helpTimerFired(data):
    """ Once the Help screen is invoked, generate the rolling text effect. The
    text is painted "Green" if it is scrolling towards right, and "Medium Violet
    Red" if is is scrolling to the left.

    Also, the direction of the text each time, it crosses a distance
    WIDTH_OFFSET / 2 away from the vertical boundary of the screen.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.scrollingRight:
        data.fontColor = "Green"
        if data.hx < data.width + WIDTH_OFFSET:
            data.hx += WIDTH_OFFSET / 2
        else:
            data.scrollingRight = False
    else:
        data.fontColor = "medium violet red"
        if data.hx > - WIDTH_OFFSET:
            data.hx -= WIDTH_OFFSET / 2
        else:
            data.scrollingRight = True

def helpRedrawAll(canvas, data):
    """ Display the scrolling text on the Help Screen.

    Note: The scrolling effect is generated in the helpTimerFired function.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """
    canvas.create_text(data.hx,
                       data.height / 2 - HEIGHT_OFFSET,
                       font="Arial " + str(2 * HELP_SCREEN_FIXED_FONT_SIZE) +
                            " bold underline",
                       text="This is not very helpful!",
                       fill=data.fontColor)

    canvas.create_text(data.width / 2,
                       data.height - 4 * HEIGHT_OFFSET,
                       font="Arial " + str(HELP_SCREEN_FIXED_FONT_SIZE),
                       text="Press mouse to return to caller's mode")

#------------------------------------------#
#             Game Over Mode               #
#------------------------------------------#
def gameOverMousePressed(event, data):
    """ If a Mouse click is detected on the Game Over screen, reset the board
    and go back to the Splash Screen.

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    data.mode = "splashScreen"
    resetBoard(data)

def gameOverKeyPressed(event, data):
    """ If a Key press is detected on the Game Over screen, reset the board and
    go back to the Splash Screen.

    :param event: A Key Press Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    data.mode = "splashScreen"
    resetBoard(data)

def gameOverTimerFired(data):
    """ Dummy Function.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    pass

def gameOverRedrawAll(canvas, data):
    """ Display the Game Over message on the screen.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    canvas.create_text(data.width / 2,
                       data.height / 3,
                       font="Arial " + str(GAME_OVER_FIXED_FONT_SIZE) + " bold",
                       text="Game Over!!!")

    canvas.create_text(data.width / 2,
                       2 * data.height / 3,
                       font="Arial " + str(GAME_OVER_FIXED_FONT_SIZE) + " bold",
                       text="You Lose :-(")

    canvas.create_text(data.width / 2,
                       data.height - 4 * HEIGHT_OFFSET,
                       font="Arial " + str(HELP_SCREEN_FIXED_FONT_SIZE),
                       text="Press key or mouse to start over")

#------------------------------------------#
#             Win Game Mode                #
#------------------------------------------#
def winGameMousePressed(event, data):
    """ If a Mouse click is detected on the 'Win Game' screen, reset the board
    and go back to the Splash Screen.

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    data.mode = "splashScreen"
    resetBoard(data)

def winGameKeyPressed(event, data):
    """ If a Key press is detected on the 'Win Game' screen, reset the board and
    go back to the Splash Screen.

    :param event: A Key Press Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    data.mode = "splashScreen"
    resetBoard(data)

def winGameTimerFired(data):
    """ Dummy Function.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    pass

def winGameRedrawAll(canvas, data):
    """ Display the Game Over message on the screen.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    canvas.create_text(data.width / 2,
                       data.height / 3,
                       font="Arial " + str(GAME_OVER_FIXED_FONT_SIZE) + " bold",
                       text="Game Over!!!")

    canvas.create_text(data.width / 2,
                       2 * data.height / 3,
                       font="Arial " + str(GAME_OVER_FIXED_FONT_SIZE) + " bold",
                       text="You Win!!!!")

    canvas.create_text(data.width / 2,
                       data.height - 4 * HEIGHT_OFFSET,
                       font="Arial " + str(HELP_SCREEN_FIXED_FONT_SIZE),
                       text="Press key or mouse to start over")

#-----------------------------------#
#          Mode dispatcher          #
#-----------------------------------#
def mousePressed(event, data):
    """ Extract mouse location via event.x, event.y; modify data based on mouse
    press location

    :param event: A Mouse Click Event
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.mode == "splashScreen":
        splashScreenMousePressed(event, data)
    elif data.mode == "playGame":
        playGameMousePressed(event, data)
    elif data.mode == "help":
        helpMousePressed(event, data)
    elif data.mode == "gameOver":
        gameOverMousePressed(event, data)
    elif data.mode == "winGame":
        winGameMousePressed(event, data)

def keyPressed(event, data):
    """Extract char and/or keysym from event.char and event.keysym; modify data
    based on key pressed.

    :param event: Key Press event captured.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.mode == "splashScreen":
        splashScreenKeyPressed(event, data)
    elif data.mode == "playGame":
        playGameKeyPressed(event, data)
    elif data.mode == "help":
        helpKeyPressed(event, data)
    elif data.mode == "gameOver":
        gameOverKeyPressed(event, data)
    elif data.mode == "winGame":
        winGameKeyPressed(event, data)

def timerFired(data):
    """ Modify data based on elapsed time.

    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.mode == "splashScreen":
        splashScreenTimerFired(data)
    elif data.mode == "playGame":
        playGameTimerFired(data)
    elif data.mode == "help":
        helpTimerFired(data)
    elif data.mode == "gameOver":
        gameOverTimerFired(data)
    elif data.mode == "winGame":
        winGameTimerFired(data)

def redrawAll(canvas, data):
    """ Redraw all canvas elements from back to front based on values in data.

    :param canvas: Canvas, on which the grid is displayed.
    :param data: 'Struct' data type bundling together named data items.
    :return: None
    """

    if data.mode == "splashScreen":
        splashScreenRedrawAll(canvas, data)
    elif data.mode == "playGame":
        playGameRedrawAll(canvas, data)
    elif data.mode == "help":
        helpRedrawAll(canvas, data)
    elif data.mode == "gameOver":
        gameOverRedrawAll(canvas, data)
    elif data.mode == "winGame":
        winGameRedrawAll(canvas, data)

def run(width, height):
    """ Creates canvas and data; registers event handlers; calls init; starts
    timer; etc.

    :param width: Width of the canvas.
    :param height: Height of the canvas
    :return: None
    """

    # Note that the wrapper functions are defined INSIDE The run function!

    """ Creates canvas and data; registers event handlers; calls init; starts
    timer; etc.

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
    data.timerDelay = SCREEN_REFRESH_INTERVAL #milliseconds
    data.width = width
    data.height = height

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

run(400, 400)