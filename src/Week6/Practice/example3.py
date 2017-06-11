from tkinter import *
####################################
# customize these functions
####################################

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def init(data):
    #Step Size
    data.stepSize = 1

    #Square
    data.squareWidth = 50
    data.squareLeft = data.width  * 0.25
    data.squareTop = data.height * 0.25
    data.fillColor = rgbString(253, 212, 34)

    #Circle
    data.circleCenters = []
    data.radius = 25

    #Timer
    data.timerCounter = 0
    data.timerDelay = 10 # Milliseconds

    #Box Animation
    data.headingRight = True
    data.headingDown = True
    data.isPaused = False

def mousePressed(event, data):
    circleCenter = (event.x, event.y)
    data.circleCenters.append(circleCenter)

def keyPressed(event, data):

    if event.keysym == 'Left':
        data.squareLeft -= data.stepSize
        print("data.squareLeft", data.squareLeft)

        if data.squareLeft + data.squareWidth < 0:
            data.squareLeft = data.width
            print("data.squareLeft", data.squareLeft)

    elif event.keysym == 'Right':
        data.squareLeft += data.stepSize

        print("data.squareLeft", data.squareLeft)

        if data.squareLeft > data.width:
            # 2 added for smoother scrolling effect.
            data.squareLeft = data.squareWidth * (-1)
            print("data.squareLeft", data.squareLeft)

    elif event.keysym == "d":
        if data.circleCenters:
            data.circleCenters.pop()

    elif event.keysym == "p":
        if data.isPaused:
            data.isPaused = False
        else:
            data.isPaused = True

def moveRight(data):
    data.squareLeft += data.stepSize

def moveLeft(data):
    data.squareLeft -= data.stepSize

def moveDown(data):
    data.squareTop += data.stepSize

def moveUp(data):
    data.squareTop -= data.stepSize

def doStep(data):

    if data.headingRight:
        if data.squareLeft + data.squareWidth > data.width:
            data.headingRight = False
        else:
            moveRight(data)
    else:
        if data.squareLeft < 0:
            data.headingRight = True
        else:
            moveLeft(data)

    if data.headingDown:
        if data.squareTop + data.squareWidth > data.height:
            data.headingDown = False
        else:
            moveDown(data)
    else:
        if data.squareTop < 0:
            data.headingDown = True
        else:
            moveUp(data)

def timerFired(data):
    data.timerCounter += 1

    if not data.isPaused:

        if data.timerCounter % 250 == 0:
            if data.fillColor == rgbString(253, 212, 34):
                data.fillColor = rgbString(199, 57, 103)
            else:
                data.fillColor = rgbString(253, 212, 34)

        doStep(data)

def redrawAll(canvas, data):
    #Draw a square box
    canvas.create_rectangle(data.squareLeft, data.squareTop,
                            data.squareLeft + data.squareWidth,
                            data.squareTop  + data.squareWidth,
                            fill=data.fillColor)

    # Draw the circles
    for cx, cy in (data.circleCenters):
        canvas.create_oval(cx - data.radius, cy - data.radius,
                           cx + data.radius, cy + data.radius,
                           fill=rgbString(199, 57, 103))

    #Add text on screen
    canvas.create_text(data.width / 2, 40,
                       text="Mouse clicks create circles")
    canvas.create_text(data.width / 2, 60,
                       text="Pressing 'd' deletes circles")
    canvas.create_text(data.width / 2, 80,
                       text="Left arrow moves square left")
    canvas.create_text(data.width / 2, 100,
                       text="Right arrow moves square right")
    canvas.create_text(data.width / 2, 120,
                       text="Timer changes color of square")
    canvas.create_text(data.width / 2, 140,
                       text="Pressing 'p' pauses/un-pauses timer")


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
