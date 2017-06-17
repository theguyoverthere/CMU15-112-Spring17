from tkinter import *
import random

def init(data):
    data.margin = 5
    data.lastKey = None
    data.snake=[(random.randint(0, data.rows - 1),
                 random.randint(0, data.cols - 1))]

    data.direction = [            (-1, 0),
                       (0, -1),               (0, +1),
                                  (+1, 0)]

    data.food = placeFood(data)
    data.gameOver = False

def isSafeMove(direction, data):
    dRow, dCol = direction

    #Locate the head
    xh, yh = data.snake[len(data.snake) - 1]

    # Movement within bounds
    if ((0 <= (xh + dRow) <= data.rows - 1) and
        (0 <= (yh + dCol) <= data.cols - 1) and

        # Head does not crash into the snake itself
        ((xh + dRow, yh + dCol) not in data.snake)):

        return True

    return False

def moveSnake(direction, data):
    dRow, dCol = direction
    xh, yh = data.snake[len(data.snake) - 1]

    if not data.gameOver:
        if isSafeMove(direction, data):
            data.snake.append((xh + dRow, yh + dCol))

            if data.food  == (xh + dRow, yh + dCol):
                # Do not remove tail, because the snake grows after
                # eating food. Also, place food again.
                data.food = placeFood(data)
            else:
                data.snake.pop(0)
        else:
            data.gameOver = True


def keyPressed(event, data):
    data.lastKey = event.keysym

def timerFired(data):
    if data.lastKey == 'Up':
        moveSnake(data.direction[0], data)
    elif data.lastKey == 'Left':
        moveSnake(data.direction[1], data)
    elif data.lastKey == 'Right':
        moveSnake(data.direction[2], data)
    elif data.lastKey == 'Down':
        moveSnake(data.direction[3], data)

def mousePressed(event, data):
    pass

def drawGameOver(canvas, data):
    if data.gameOver:
        canvas.create_text(data.width/2, data.height/2, text="Game over!",
                           font="Arial 26 bold")

def getCellBounds(row, column, data):
    x0 = data.margin
    y0 = data.margin

    rowHeight = (data.height - (2 * data.margin)) / data.rows
    colWidth = (data.width - (2 * data.margin)) / data.cols

    xn = x0 + column * colWidth
    yn = y0 + row * rowHeight

    return xn, yn, (xn + colWidth), (yn + rowHeight)

def drawCell(canvas, x0, y0, xn, yn, color):

    if color == "orange" or color == "green":
        canvas.create_oval(x0, y0, xn, yn, fill=color)
        canvas.create_rectangle(x0, y0, xn, yn)
    else:
        canvas.create_rectangle(x0, y0, xn, yn, fill=color)

def drawBoard(canvas, data):
    for row in range(data.rows):
        for column in range(data.cols):
            (x0, y0, xn, yn) = getCellBounds(row, column, data)
            drawCell(canvas, x0, y0, xn, yn, color="white")

def drawSnake(canvas, data):
    for (row, column) in data.snake:
        (x0, y0, xn, yn) = getCellBounds(row, column, data)
        drawCell(canvas, x0, y0, xn, yn, color="orange")

def placeFood(data):

    x0, y0 = random.randint(0, data.rows - 1), random.randint(0, data.cols - 1)

    while (x0, y0) in data.snake:
        x0, y0 = (random.randint(0, data.rows - 1),
                  random.randint(0, data.cols - 1))

        data.food = (x0, y0)

    return x0, y0

def drawFood(canvas, data):
    row, column = data.food

    (x0, y0, xn, yn) = getCellBounds(row, column, data)
    drawCell(canvas, x0, y0, xn, yn, color="green")

def redrawAll(canvas, data):
    drawBoard(canvas, data)
    drawSnake(canvas, data)
    drawFood(canvas, data)
    drawGameOver(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300, rows=10, columns=10):

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
    # bundling together a few named data items. An empty class definition will
    # do nicely.
    # https://stackoverflow.com/questions/1878710/struct-objects-in-python/1878775#1878775
    class Struct(object):
        pass

    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 150 #milliseconds
    data.rows = rows
    data.cols = columns

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

run(400, 400, 10, 10)


