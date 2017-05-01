#******************************************************************************#
# Author: Tarique Anwer
# Date:   30/4/2017
# Description: Draw Clocks as displayed in the diagram.
#******************************************************************************#
from tkinter import *
import math

def drawClock(canvas, x0, y0, x1, y1, hour, minute):
    """Draws a clock with the specified time.

    Given the top-left and bottom-right rectangle coordinate, the function
    draws a Clock on the canvas.

    :param canvas: Canvas on which the graphics will be displayed.
    :param x0: Top left corner x-coordinate
    :param y0: Top left corner y-coordinate
    :param x1: Bottom right corner x-coordinate
    :param y1: Bottom right corner y-coordinate

    :return: None
    """

    # Create the outer rectangle
    canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=1)

    #Create the inner circle
    width  = x1 - x0
    height = y1 - y0
    r = min(width, height) / 2
    cx = x0 + width/2
    cy = y0 + height/2

    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="black", width=2)

    #Create the hour hand
    hourAngle = (math.pi / 2) - (2 * math.pi) * (hour / 12)
    hourRadius = r / 2
    hourX = cx + hourRadius * math.cos(hourAngle)
    hourY = cy - hourRadius * math.sin(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY)

    #Create the minute hand
    minuteAngle = (math.pi / 2) - (2 * math.pi) * (minute / 60)
    minuteRadius = r * 0.85
    minuteX = cx + minuteRadius * math.cos(minuteAngle)
    minuteY = cy - minuteRadius * math.sin(minuteAngle)
    canvas.create_line(cx, cy, minuteX, minuteY)

def draw(canvas, width, height):
    drawClock(canvas, 25, 25, 175, 150, 2, 30)
    drawClock(canvas, 75, 160, 125, 200, 2, 30)

    clockWidth = 40
    clockHeight = 40
    margin = 5
    hour = 1

    for row in range(3):
        for column in range(4):
            left = 200 + (column * clockWidth) + margin
            top  = 50  + (row * clockHeight) + margin
            right = left + clockWidth - margin
            bottom = top + clockHeight - margin

            drawClock(canvas, left, top, right, bottom, hour, 0)
            hour += 1

def runDrawing(width=500, height=500):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()

runDrawing()