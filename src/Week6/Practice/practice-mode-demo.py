from tkinter import *
####################################
# customize these functions
####################################

def init(data):
    data.mode = "splashScreen"
    data.score = 0

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if data.mode == "splashScreen":
        splashScreenMousePressed(event, data)
    elif data.mode == "playGame":
        playGameMousePressed(event, data)
    elif data.mode == "help":
        helpMousePressed(event, data)

def keyPressed(event, data):
    if data.mode == "splashScreen":
        splashScreenKeyPressed(event, data)
    elif data.mode == "playGame":
        playGameKeyPressed(event, data)
    elif data.mode == "help":
        helpKeyPressed(event, data)

def timerFired(data):
    if data.mode == "splashScreen":
        splashScreenTimerFired(data)
    elif data.mode == "playGame":
        playGameTimerFired(data)
    elif data.mode == "help":
        helpTimerFired(data)

def redrawAll(canvas, data):
    if data.mode == "splashScreen":
        splashScreenRedrawAll(canvas, data)
    elif data.mode == "playGame":
        playGameRedrawAll(canvas, data)
    elif data.mode == "help":
        helpRedrawAll(canvas, data)

####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    pass

def splashScreenKeyPressed(event, data):
    data.mode = "playGame"

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2 - 20,
                       text="This is a splash screen!", font="Arial 26 bold")

    canvas.create_text(data.width / 2, data.height / 2 + 20,
                       text="Press any key to play", font="Arial 20")

####################################
# playGame mode
####################################

def playGameMousePressed(event, data):
    data.score = 0

def playGameKeyPressed(event, data):
    if event.keysym == 'h':
        data.mode = "help"

def playGameTimerFired(data):
    data.score += 1

def playGameRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2 - 40,
                       text="This is a fun game!", font="Arial 30 bold")

    score = "Score = " + str(data.score)
    canvas.create_text(data.width / 2, data.height / 2,
                       text=score, font="Arial 26")

    canvas.create_text(data.width / 2, data.height / 2 + 30,
                       text="Click anywhere to reset score.", font="Arial 20")

    canvas.create_text(data.width / 2, data.height / 2 + 60,
                       text="Press 'h' for help!", font="Arial 20")

####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    pass

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2 - 40,
                       text="This is help mode!", font="Arial 26 bold")

    canvas.create_text(data.width/2, data.height/2 - 10,
                       text="How to play:", font="Arial 20")

    canvas.create_text(data.width/2, data.height/2 + 15,
                       text="Do nothing and score points!", font="Arial 20")

    canvas.create_text(data.width/2, data.height/2 + 40,
                       text="Press any key to keep playing!", font="Arial 20")

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
