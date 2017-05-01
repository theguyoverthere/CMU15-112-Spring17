#******************************************************************************#
# Author: Tarique Anwer
# Date:   1/5/2017
# Description: Write the function drawTiledFlags that takes the parameters
#              (margin, rows, cols, flagWidth, flagHeight) and draws a
#              rows-by-cols grid of flags of the given dimension, with the given
#              margin around the whole grid, and with the window sized to just
#              fit around the grid with the given margin. The flags should
#              alternate in a checkerboard pattern between the flag of the
#              European Union (with circles drawn in place of stars) and the
#              flag of the Bahamas, with the EU flag in the left-top corner.
#              You do not have to exactly color match, but the blue in the
#              Bahamas flag must be obviously lighter than the blue in the EU
#              flag. Also, your black triangle in the Bahamas flag does not have
#              to match proportions exactly, just reasonably closely. The same
#              goes for the circles in the EU flag, just be reasonably close.
#              For example, this call:
#              drawTiledFlags(margin=10, rows=3, cols=5,
#                             flagWidth=100, flagHeight=60) produces this result
#              http://www.kosbie.net/cmu/fall-14/15-112/notes/hw3.html
#******************************************************************************#
from tkinter import *
import math

def rgbString(red, green, blue):
    """ Convert RBG integer values to hexadecimal string

    :param red: Red component of RGB as integer
    :param green: Green component of RGB as integer
    :param blue: Blue component of RGB as integer

    :return: Hexadecimal string representation of RGB colors

    """
    return "#%02x%02x%02x" % (red, green, blue)

def drawEuropeanUnionFlag(canvas, x0, y0, x1, y1):
    """ Draws the European Union Flag.

    Draws the EU flag except with the stars replaced by circles. The precise
    specification of the circles are arbitrary and only a close approximation
    of the real thing.

    :param canvas: Canvas on which the flag should be drawn.
    :param x0: x-coordinate of the top-left corner of the flag.
    :param y0: y-coordinate of the top-left corner of the flag.
    :param x1: x-coordinate of the bottom-right corner of the flag.
    :param y1: y-coordinate of the bottom-right corner of the flag.

    :return: None

    """
    pantoneBlue = rgbString(0,51,153)
    pantoneYellow = rgbString(255,204,0)
    canvas.create_rectangle(x0, y0, x1, y1, fill=pantoneBlue)

    width  = x1 - x0
    height = y1 - y0
    cx, cy, outerRadii = x0 + width/2, y0 + height/2, min(width, height) / 3

    outerRadii *= 0.85
    circleRadii = 2.5

    for hour in range(12):
        hourAngle = (math.pi / 2) -  (2 * math.pi) * (hour / 12)
        hourX = cx + outerRadii * math.cos(hourAngle)
        hourY = cy - outerRadii * math.sin(hourAngle)
        canvas.create_oval(hourX - circleRadii, hourY - circleRadii,
                           hourX + circleRadii, hourY + circleRadii,
                           fill=pantoneYellow)

def drawBahamaFlag(canvas, x0, y0, x1, y1):
    """Draws the Flag of Bahamas.

    Draws the flag of Bahamas. The precise specification of the flag is
    arbitrary and only a close approximation of the real thing.

    :param canvas: Canvas on which the flag should be drawn.
    :param x0: x-coordinate of the top-left corner of the flag.
    :param y0: y-coordinate of the top-left corner of the flag.
    :param x1: x-coordinate of the bottom-right corner of the flag.
    :param y1: y-coordinate of the bottom-right corner of the flag.

    :return: None
    """
    tiffanyBlue = rgbString(0,171,201)
    bananaYellow = rgbString(250,224,66)
    canvas.create_rectangle(x0, y0, x1, y1, fill=tiffanyBlue)

    width =  x1 - x0
    height = y1 - y0
    canvas.create_rectangle(x0, y0 + height /3,
                            x1, y1 - height /3,
                            fill=bananaYellow)

    canvas.create_polygon(x0, y0,
                          x0 + 0.4 * width,
                          y0 + 0.5 * height,
                          x0, y1,
                          fill="black")

def drawTiledFlags(margin, rows, cols, flagWidth, flagHeight):
    """ Draws a tiled flag consisting of EU and Bahama's flags.

    The function drawTiledFlags draws a rows-by-cols grid of flags of the given
    dimension, with the given margin around the whole grid, and with the window
    sized to just fit around the grid with the given margin.
        The flags alternate in a checkerboard pattern between the flag of the
    European Union (with circles drawn in place of stars) and the flag of the
    Bahamas, with the EU flag in the left-top corner.

    :param margin: White space width all round the grid of tiles.
    :param rows: No of rows of the tiles.
    :param cols: No of columns of the tiles.
    :param flagWidth: Width of each flag in the tile.
    :param flagHeight: Height of each flag in the tile.

    :return: None
    """

    canvasWidth  = (cols * flagWidth) + (2 * margin)
    canvasHeight = (rows * flagHeight)  + (2 * margin)

    root = Tk()
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()

    for row in range(rows):
        # For every even row, every even column has a EU flag.
        # For every odd row, every odd column has a EU flag.
        for column in range(cols):

            left = margin + (column * flagWidth)
            top  = margin + (row * flagHeight)
            right = left + flagWidth
            bottom = top + flagHeight

            if ((row % 2 == 0 and column % 2 == 0) or
                (row % 2 == 1 and column % 2 == 1)):
                drawEuropeanUnionFlag(canvas, left, top, right, bottom)
            else:
                drawBahamaFlag(canvas, left, top, right, bottom)

    root.mainloop()

drawTiledFlags(margin=10, rows=3, cols=5, flagWidth=100, flagHeight=60)