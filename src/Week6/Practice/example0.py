# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    pass

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
