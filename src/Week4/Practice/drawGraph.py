#******************************************************************************#
# Author: Tarique Anwer
# Date:   4/5/2017
# Description:  Write the function drawGraph that takes the parameters
#               (winWidth, winHeight, fn, xmax, xstep, ymax, ystep), and then:
#               1. It creates a window of the given dimensions.
#               2. And it graphs the given function (which is a normal Python
#                  function, which you may assume takes one variable, a float,
#                  and returns a float result).
#               3. The graph needs to be scaled, so that the center of the graph
#                  is still (0,0), but the rightmost point of the x axis is at
#                  (xmax,0), and the xmin value is -xmax, so the leftmost point
#                  of the x axis is at (-xmax, 0). Similarly, ymax describes the
#                  extent of the y axis. To do this, you will want to compute a
#                  scaling factor for each dimension. For this, consider that
#                  the distance from xmin to xmax in the actual graph
#                  corresponds to the number of horizontal pixels in your
#                  window.
#               4. The graph needs to have hash marks along the axes, as
#                  indicated by the given xstep and ystep values. The hash marks
#                  need to be labeled, with the x axis labels just below the
#                  hash marks, and the y axis labels just to the left of the
#                  hashmarks. Note: for hashmarks, you do not have to worry
#                  about the "boundary conditions", in that you may or may not
#                  include the last hashmark in each direction (this may make
#                  the math just a bit easier in some cases).
#               5. The graph needs a title, centered in a bold 40-point Arial
#                  font. The title should be obtained by fn.__name__ (Python
#                  adds this field automatically to every function defined using
#                  "def").
#               For example, this call:
#               def cosineInDegrees(degrees):
#                   return math.cos(math.radians(degrees))
#
#               drawGraph(winWidth=600,winHeight=300,
#                         fn=cosineInDegrees,
#                         xmax=+720, xstep=90,
#                         ymax=+3, ystep=1) produces this result:
#               http://www.kosbie.net/cmu/fall-14/15-112/notes/hw3.html
#******************************************************************************#
from tkinter import *
import math

def addTitle(canvas, xc, yc, title, font):
    """ Add title to canvas

    :param canvas: Canvas on which the title should be added.
    :param xc: x-coordinate of the centre of canvas
    :param yc: y-coordinate of the centre of canvas
    :param title: Title of the graph
    :param font: Text font
    :return: None
    """
    canvas.create_text(xc, yc, text = title, font = font)

def drawAxes(canvas, winWidth, winHeight, xMax, xStep, yMax, yStep):
    """ Draw the axes for the graph

    Draw the horizontal and vertical axes as per scale.

    :param canvas: Canvas on which the title should be added.
    :param winWidth: Window width
    :param winHeight: Window height
    :param xMax: Rightmost pixel of the scaled graph.
    :param xStep: Step size used for drawing horizontal hash marks.
    :param yMax: Top-most pixel of the scaled graph.
    :param yStep: Step size used for drawing vertical hash marks.
    :return: None
    """

    # Scale the graph - Compute Pixels per unit on the graph.
    (cx, cy) = (winWidth / 2, winHeight / 2)
    xPixels = winWidth  / (2 * xMax)
    yPixels = winHeight / (2 * yMax)

    #Draw the axes and the hash marks.
    hashLen = 5
    noVerticalHash = int(2 * yMax / yStep)
    noHorizontalHash = int(2 * xMax / xStep)

    #Draw the Horizontal and Vertical axes
    canvas.create_line(0, cy, winWidth, cy)
    canvas.create_line(cx, 0, cx, winHeight)

    # Draw the horizontal hash marks.
    for j in range(noHorizontalHash):
        hx = j * xPixels * xStep
        screenX = (j * xStep) - xMax
        canvas.create_line(hx, cy - hashLen, hx, cy + hashLen)

        if abs(screenX) != xMax:
            canvas.create_text(hx, cy + 2 * hashLen, text = str(int(screenX)))

    # Draw the vertical hash marks.
    for i in range(noVerticalHash):
        hy = i * yPixels * yStep
        screenY =  yMax - (i * yStep)
        canvas.create_line(cx - hashLen, hy, cx + hashLen, hy)

        if abs(screenY) != yMax:
            canvas.create_text(cx - 2 * hashLen, hy, text = str(int(screenY)))

def plotPoints(canvas, winWidth, winHeight, fn, xMax, yMax):
    """ Plot the points on the graph for the function fn

    :param canvas: Canvas on which the points need to be plotted.
    :param winWidth: Window width.
    :param winHeight: Window height.
    :param fn: Name of the function to be plotted.
    :param xMax: Rightmost pixel of the scaled graph.
    :param yMax: Top-most pixel of the scaled graph.
    :return: None
    """

    # Compute the (0, 0) location of the graph.
    (cx, cy) = (winWidth / 2, winHeight / 2)

    # Compute the pixels per unit graph, along x and y axes
    xPixels = winWidth  / (2 * xMax)
    yPixels = winHeight / (2 * yMax)

    # Plot the points using straight lines.
    oldScreenX = oldScreenY = None
    for screenX in range(winWidth):

        # Scale from pixels to graph units and back to pixels.
        x = (screenX - cx) * (1 / xPixels)
        y = fn(x) * yPixels
        screenY = cy - y

        if oldScreenX is not None:
            canvas.create_line(oldScreenX, oldScreenY, screenX, screenY, fill="blue")

        (oldScreenX, oldScreenY) = (screenX, screenY)

def drawGraph(winWidth, winHeight, fn, xmax, xstep, ymax, ystep):
    """ Draw the specified graph

        The function drawGraph:
        1. Creates a window of the given dimensions.

        2. And graphs the given function (which is a normal Python
           function, that takes one variable, a float and returns a float
           result).

        3. The graph is scaled, so that the center of the graph is still (0,0),
           but the rightmost point of the x axis is at (xmax,0), and the xmin
           value is -xmax, so the leftmost point of the x axis is at (-xmax, 0).
           Similarly, ymax describes the extent of the y axis.

        4. The graph has hash marks along the axes, as indicated by the given
           xstep and ystep values. The hash marks are labeled, with the x axis
           labels just below the hash marks, and the y axis labels just to the
           left of the hashmarks. (The boundary conditions can be ignored)

        5. The title of the graph is centered in a bold 40-point Arial
           font.

    :param winWidth: Window width.
    :param winHeight: Window height.
    :param fn: Name of the function to be plotted.
    :param xmax: Rightmost pixel of the scaled graph.
    :param xstep: Step size used for drawing horizontal hash marks.
    :param ymax: Top-most pixel of the scaled graph.
    :param ystep: Step size used for drawing vertical hash marks.
    :return: None
    """

    # Create a window of the given dimensions
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    # Add the title to the canvas
    xTitle = winWidth /2
    yTitle = 25
    font = "Arial 34 bold"
    addTitle(canvas, xTitle, yTitle, fn.__name__, font)

    # Scale the graph and draw the Horizontal and Vertical Axes
    drawAxes(canvas, winWidth, winHeight, xmax, xstep, ymax, ystep)

    # Plot the points
    plotPoints(canvas, winWidth, winHeight, fn, xmax, ymax)

    # Display the graph on the canvas
    root.mainloop()


# Test the function
def cosineInDegrees(degrees):
    return math.cos(math.radians(degrees))

drawGraph(winWidth=600,winHeight=300,
          fn=cosineInDegrees,
          xmax=+720, xstep=90,
          ymax=+3, ystep=1)

def strangeFunction(x):
    if (int(round(x)) % 2 == 0):
        return x+5*math.cos(x)**3
    else:
        return 10*math.sin(x/2)

drawGraph(winWidth=600,winHeight=300,
          fn=strangeFunction,
          xmax=+20, xstep=4,
          ymax=+15, ystep=3)