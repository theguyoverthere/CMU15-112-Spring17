from tkinter import *
####################################
# customize these functions
####################################

def init(data):
    data.rows = 4
    data.cols = 8
    data.margin = 10
    data.selection = (-1, -1)

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    row, col = getCell(event.x, event.y, data)

    if data.selection == (row, col):
        data.selection = (-1, -1)
    else:
        data.selection = (row, col)

def withinBounds(row, col, data):

    if (row < 0 or row > data.rows - 1 or
        col < 0 or col > data.cols - 1):
        return False

    return True

def getCell(xn, yn, data):
    x0 = data.margin
    y0 = data.margin

    rowHeight = (data.height - (2 * data.margin)) / data.rows
    colWidth = (data.width - (2 * data.margin)) / data.cols

    column = (xn - x0) // colWidth
    row = (yn - y0) // rowHeight

    if withinBounds(row, column, data):
        return row, column

    return -1, -1

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def getCellBounds(row, column, data):
    x0 = data.margin
    y0 = data.margin

    rowHeight = (data.height - (2 * data.margin)) / data.rows
    colWidth = (data.width - (2 * data.margin)) / data.cols

    xn = x0 + column * colWidth
    yn = y0 + row * rowHeight

    return xn, yn, (xn + colWidth), (yn + rowHeight)

def drawCell(canvas, x0, y0, xn, yn, color):

    canvas.create_rectangle(x0, y0, xn, yn, fill=color)

def drawGrid(canvas, data):

    for row in range(data.rows):
        for column in range(data.cols):
            (x0, y0, xn, yn) = getCellBounds(row, column, data)

            fillColor = "orange" if (row, column) == data.selection else "cyan"
            drawCell(canvas, x0, y0, xn, yn, fillColor)

def redrawAll(canvas, data):
    drawGrid(canvas, data)

    canvas.create_text(data.width / 2, data.height / 2 - 20,
                       text="Click in cells!",
                       font="Arial 26 bold",
                       fill="darkBlue")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):

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
    data.timerDelay = 100 #milliseconds

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
    print("bye!")

run(400, 200)
