#******************************************************************************#
# Author: Tarique Anwer
# Date:   2/5/2017
# Description: Write the function drawBlankSheetMusic that takes the parameters
#              (title, winWidth, winHeight, lineHeight, lineMargin,
#              measuresPerLine) and draws as many lines of blank sheet music
#              that can fit in the given sized window.
#              The title is given as a string, which should be drawn in 20-point
#              Arial bold font, horizontally centered 25 pixels below the top of
#              the window.
#              The top of the first line should be at 50 pixels from the window
#              top. Each row, or line, is actually called a "staff line". It is
#              made up of 5 separate horizontal lines (see picture below for
#              details). As an aside: you do not need to read music to do this
#              exercise, but most of you probably know that these lines
#              correspond to the notes E-G-B-D-F, from bottom to top.
#              In any case, the vertical distance from the top line to the
#              bottom line in one row is the given lineHeight. The vertical
#              distance between the bottom line of one row and the top line of
#              the next row is the lineMargin. This is also the horizontal
#              distance between the edges of each row and the left and right
#              edges of the window. Finally, each row is split up by vertical
#              lines into measures, according to the given measuresPerLine. For
#              example, this call:drawBlankSheetMusic(title="Blank sheet music",
#              winWidth=800, winHeight=200,lineHeight=50, lineMargin=20,
#              measuresPerLine=5) produces this result:
#              http://www.kosbie.net/cmu/fall-14/15-112/notes/hw3.html
#******************************************************************************#
from tkinter import *
import decimal

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def drawStaffLines(canvas, yLine, xLeft, xRight, lineSeparation):
    numDetailLines = 5

    # Draw the Horizontal Lines
    for i in range(numDetailLines):
        canvas.create_line(xLeft, yLine, xRight, yLine)
        yLine += lineSeparation

def drawVerticalLines(canvas, x, yTop, yBottom):
    canvas.create_line(x, yTop, x, yBottom)

def drawBlankSheetMusic(title, winWidth, winHeight,
                        lineHeight, lineMargin, measuresPerLine):
    """ Draws a blank Music Sheet.
    The function drawBlankSheetMusic draws as many lines of blank sheet music
    that can fit in the given sized window.

    The title is given as a string, which should be drawn in 20-point Arial bold
    font, horizontally centered 25 pixels below the top of the window.
    The top of the first line should be at 50 pixels from the window top. Each
    row, or line, is actually called a "staff line". It is made up of 5 separate
    horizontal lines (see picture below for details).
    The vertical distance from the top line to the bottom line in one row is the
    given lineHeight. The vertical distance between the bottom line of one row
    and the top line of the next row is the lineMargin. This is also the
    horizontal distance between the edges of each row and the left and right
    edges of the window.
    Finally, each row is split up by vertical lines into measures, according to
    the given measuresPerLine. For example, this call:drawBlankSheetMusic(title=
    "Blank sheet music",winWidth=800, winHeight=200,lineHeight=50,
    ineMargin=20, measuresPerLine=5) produces this result:
    http://www.kosbie.net/cmu/fall-14/15-112/notes/hw3.html

    :param title: Title to displayed at the top.
    :param winWidth: Width of the canvas window.
    :param winHeight: Height of the canvas window.
    :param lineHeight: The vertical distance from the top line to the bottom
     line in one row.
    :param lineMargin: The vertical distance between the bottom line of one row
     and the top line of the next row.
    :param measuresPerLine: Each row is split up into measurePerLine columns.
    :return:None
    """

    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    # Add the title to the canvas
    xTitle = winWidth /2
    yTitle = 25
    font = "Arial 16 bold"
    canvas.create_text(xTitle, yTitle, text = title, font = font)

    # Draw the StaffLines
    numStaffLine = int(winHeight/ (lineHeight + lineMargin))
    numDetailLines = 5
    lineSeparation = lineHeight / (numDetailLines - 1)

    for i in range(numStaffLine):
        yTopStaffLine = (2 * yTitle) + (i * (lineHeight + lineMargin))
        drawStaffLines(canvas,
                       yTopStaffLine,
                       lineMargin,
                       winWidth - lineMargin,
                       lineSeparation)

        #Draw the vertical lines
        for j in range(measuresPerLine + 1):
            separation = (winWidth - (2 * lineMargin)) / measuresPerLine
            xVertical = lineMargin + (j * separation)

            drawVerticalLines(canvas,
                              xVertical,
                              yTopStaffLine,
                              yTopStaffLine + lineHeight)


    root.mainloop()

drawBlankSheetMusic(title="Blank sheet music", winWidth=800, winHeight=200,
                    lineHeight=50, lineMargin=20, measuresPerLine=5)