#******************************************************************************#
# Author: Tarique Anwer
# Date:   6/5/2017
# Description: Write the function drawGrid that takes 5 values – a canvas, a
#              left, top, right, and bottom – describing a rectangular region of
#              the canvas, and fills this region with a drawing of a rectangular
#              grid.  For large areas (>200 pixels wide), the grid should have 4
#              rows and 8 columns, with cells alternating in the shades of red
#              and blue in the image below(or fairly close to them in any case).
#              For smaller areas, the grid should have 8 rows and 4 columns, and
#              the cells should alternate black and white.  Also, each cell will
#              be labeled with a number (note that you can provide a number as
#              the text value in create_text).  For large areas, the numbers
#              start in the left-top cell and proceed rightwards and then
#              downwards.  For small areas, the numbers start in the bottom-left
#              cell and proceed upwards and then rightwards. Here is a
#              screenshot to help:
#     http://www.kosbie.net/cmu/fall-13/15-112/handouts/hw2.html#drawGrid
#******************************************************************************#
from tkinter import Tk, Canvas

def rgbString(red, green, blue):
    """ Convert RBG integer values to hexadecimal string

    :param red: Red component of RGB as integer
    :param green: Green component of RGB as integer
    :param blue: Blue component of RGB as integer

    :return: Hexadecimal string representation of RGB colors

    """
    return "#%02x%02x%02x" % (red, green, blue)

def drawCell(canvas, x0, y0, x1, y1, color, text):
    """ Draw a rectangular cell.

     Draw a rectangular cell of the specified dimension and color. The cell also
     has a text label as specified.

    :param canvas: Canvas on which the cell should be drawn.
    :param x0: x-coordinate of the top left corner of the cell.
    :param y0: y-coordinate of the top left corner of the cell.
    :param x1: x-coordinate of the bottom right corner of the cell.
    :param y1: x-coordinate of the bottom right corner of the cell.
    :param color: Rectangle fill color
    :param text: Text label centered in the current cell.
    :return: None
    """
    xc = (x0 + x1) / 2
    yc = (y0 + y1) / 2

    canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    canvas.create_text(xc, yc, text=text, font="Arial 10 bold",
                       fill=rgbString(186, 27, 29)) # Carnelian Red

def drawGrid(canvas, left, top, right, bottom):
    """ Draw a grid of alternating colors.

    Takes 5 values – a canvas, a left, top, right, and bottom – describing a
    rectangular region of the canvas, and fills this region with a drawing of a
    rectangular grid.  For large areas (>200 pixels wide), the grid has
    4 rows and 8 columns, with cells alternating in the shades of red and blue
    in the image below(or fairly close to them in any case).

    For smaller areas, the grid should have 8 rows and 4 columns, and the cells
    alternate black and white.  Also, each cell is labeled with a number.  For
    large areas, the numbers start in the left-top cell and proceed rightwards
    and then downwards.  For small areas, the numbers start in the bottom-left
    cell and proceed upwards and then rightwards. Here is a screenshot to help:
    http://www.kosbie.net/cmu/fall-13/15-112/handouts/hw2.html#drawGrid

    :param canvas: Canvas on which the grid should be drawn
    :param left: x-coordinate of the top-left corner of the grid.
    :param top: y-coordinate of the top-left corner of the grid.
    :param right: x-coordinate of the bottom-right corner of the grid.
    :param bottom: y-coordinate of the bottom-right corner of the grid.
    :return: None
    """

    width = right - left
    height = bottom - top

    if width > 200 and height > 200:
        rows = 4
        columns = 8
        cellWidth = width / columns
        cellHeight = height / rows

        for row in range(rows):
            for column in range(columns):
                x0 = left + column * cellWidth
                y0 = top  + row * cellHeight
                x1 = x0 + cellWidth
                y1 = y0 + cellHeight

                if (row + column) % 2 == 0:
                    color = rgbString(255, 107, 107) #Pastel Red
                else:
                    color = rgbString(101, 88, 228) #Majorelle Blue

                text = str(row * columns + column + 1)

                drawCell(canvas, x0, y0, x1, y1, color, text)
    else:
        rows = 8
        columns = 4
        cellWidth = width / columns
        cellHeight = height / rows

        for row in range(rows):
            for column in range(columns):
                x0 = left + column * cellWidth
                y0 = top  + row * cellHeight
                x1 = x0 + cellWidth
                y1 = y0 + cellHeight

                if (row + column) % 2 == 0:
                    color = "black"
                else:
                    color = "white"

                text = str((rows - row) + rows * column)

                drawCell(canvas, x0, y0, x1, y1, color, text)

def runDrawing(left, top, right, bottom):
    """ Create the canvas for the grid.

    :param left: x-coordinate of the top-left corner of the grid.
    :param top: y-coordinate of the top-left corner of the grid.
    :param right: x-coordinate of the bottom-right corner of the grid.
    :param bottom: y-coordinate of the bottom-right corner of the grid.
    :return: None

    """
    root = Tk()
    canvas = Canvas(root, width=right, height=bottom)
    canvas.pack()

    drawGrid(canvas, left, top, right, bottom)
    root.mainloop()

# Test the function
runDrawing(200, 200, 600, 600)
runDrawing(0, 0, 200, 200)
runDrawing(0, 0, 600, 600)
