#******************************************************************************#
# Author: Tarique Anwer
# Date:   30/4/2017
# Description: Draw the Belgian Flags as displayed in the diagram.
#******************************************************************************#
from tkinter import *

def drawBelgianFlag(canvas, x0, y0, x1, y1):
    """Draws a Belgian Flag.

    Given the top-left and bottom-right rectangle coordinate, the function
    draws a Belgian Flag on the canvas. Consists of three equal sized vertical
    filled rectangles - Black on the left, yellow in the middle, Red on the
    right.

    :param canvas: Canvas on which the graphics will be displayed.
    :param x0: Top left corner x-coordinate
    :param y0: Top left corner y-coordinate
    :param x1: Bottom right corner x-coordinate
    :param y1: Bottom right corner y-coordinate

    :return: None
    """

    width = (x1 - x0)

    canvas.create_rectangle(x0, y0,                 #Top-Left
                            x0 + width / 3, y1,     #Bottom-Right
                            fill="black", width=0)  #Fill with Black

    canvas.create_rectangle(x0 + width / 3, y0,     #Top-Left
                            x0 + 2 * width / 3, y1, #Bottom-Right
                            fill="yellow", width=0) #Fill with Yellow

    canvas.create_rectangle(x0 + 2 * width /3, y0,  #Top-Left
                            x1, y1,                 #Bottom-Right
                            fill="red", width=0)    #Fill With Red


def draw(canvas, width, height):
    drawBelgianFlag(canvas, 25,25,175,150)
    drawBelgianFlag(canvas, 75,160,125,200)

    flagWidth = 30
    flagHeight = 25
    margin = 5

    for row in range(4):
        for column in range(6):
            left = 200 + (column * flagWidth) + margin
            top  = 50  + (row * flagHeight) + margin
            right = left + flagWidth - margin
            bottom = top + flagHeight - margin

            drawBelgianFlag(canvas, left, top, right, bottom)


def runDrawing(width=500, height=500):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()

runDrawing()