from tkinter import *

def drawBelgianFlag(canvas, x0, y0, x1, y1):
    # draw a Belgian flag in the area bounded by (x0, y0) in
    # the top left end and (x1, y1) in the bottom right

    width = x1 - x0
    canvas.create_rectangle(x0, y0,
                            x0 + width / 3, y1,
                            fill="black", width=0)

    canvas.create_rectangle(x0 + width / 3, y0,
                            x0 + 2 * width / 3, y1,
                            fill="yellow", width=0)

    canvas.create_rectangle(x0 + 2 * width / 3, y0,
                            x1, y1,
                            fill="red", width=0)


def draw(canvas, width, height):
    drawBelgianFlag(canvas, 25, 25, 175, 150)

     # And draw a smaller one below it
    drawBelgianFlag(canvas, 75, 160, 125, 200)

    flagWidth = 30
    flagHeight =25
    margin = 5

    for row in range(4):
        for col in range(6):
            left = 200 + col * flagWidth + margin
            top  = 50 + row * flagHeight + margin

            right = left + flagWidth - margin
            bottom = top + flagHeight - margin
            drawBelgianFlag(canvas, left, top, right, bottom)

def runDrawing(width = 300, height = 300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")

runDrawing(400, 400)