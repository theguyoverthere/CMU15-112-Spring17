from tkinter import *

def draw(canvas, width, height):
    pass

def runDrawing(width = 300, height = 300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")

runDrawing(400, 100)