#******************************************************************************#
# Author: Tarique Anwer
# Date:   6/5/2017
# Description: Write the function drawCirclePattern(n) that takes one parameter,
#              a positive int, and displays a graphics window, inside of which
#              it draws the nxn version of this picture:
#
#              http://www.kosbie.net/cmu/spring-16/15-112/notes/hw4.html
#
#              While the image above shows two circle patterns, you only need to
#              draw one at a time. For example, the left image above was drawn
#              with 10 rows (and 10 columns), and the right image with 5 rows
#             (and 5 columns). The pattern consists of "buttons" (or perhaps
#             "bullseyes"), where each button is really several circles drawn on
#              top of each other. Each circle in a "button" has a radius 2/3rds
#              as large as the next-larger circle, which continues until the
#              radius is less than 1. As for the color of each button, here are
#              the rules to follow:
#
#              Rule 1: Starting from the left-top corner, every 4th diagonal is
#                      entirely red.
#              Rule 2: For the non-red buttons, starting from the top row, every
#                      3rd row is entirely green.
#              Rule 3: For the non-red and non-green buttons, starting from the
#                      second-to-leftmost column, every 2nd column is entirely
#                      yellow.
#              Rule 4: Any non-red, non-green, and non-yellow button is blue.
#
#              Note that these rules can be fairly easily implemented using a
#              single if-elif-elif-else statement. Inside that statement, you
#              might want to set a variable, say one named "color", based on
#              each of these four conditions. Then you could draw with
#              fill=color.
#
#              Note: The drawing should mostly fill the window, and the 10x10
#              case should be about the same size as the 10x10 case in the image
#              above, but the exact dimensions of the drawing are up to you.
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

def drawButton(canvas, left, top, right, bottom, color):
    """ Draw a single button.

    The pattern consists of "buttons", where each button is really several
    circles drawn on top of each other. Each circle in a "button" has a radius
    2/3rds as large as the next-larger circle, which continues until the radius
    is less than 1.

    :param canvas: Canvas on which the button should be drawn.
    :param left: x-coordinate of the Top-Left corner of rectangle enclosing the
               circle.
    :param top: y-coordinate of the Top-Left corner of rectangle enclosing the
               circle.
    :param right: x-coordinate of the Bottom-right corner of rectangle enclosing
               the circle.
    :param bottom: y-coordinate of the Bottom-right corner of rectangle
               enclosing the circle.
    :param color: Fill color of the button
    :return: None
    """

    width = right - left
    height = bottom - top
    r = min(width, height) / 2
    cx = left + width / 2
    cy = top + height / 2

    while r > 1:
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                           outline="black", fill=color, width=1)
        r *= 2/3


def drawCirclePattern(n):
    """ Display a pattern consisting of colored circles.

    Displays a graphics window, inside of which it draws the nxn version of this
    picture: http://www.kosbie.net/cmu/spring-16/15-112/notes/hw4.html

    The pattern consists of "buttons" (or perhaps "bullseyes"), where each
    button is really several circles drawn on top of each other. Each circle in
    a "button" has a radius 2/3rds as large as the next-larger circle, which
    continues until the radius is less than 1.

    As for the color of each button, here are the rules:

    Rule 1: Starting from the left-top corner, every 4th diagonal is entirely
            red.
    Rule 2: For the non-red buttons, starting from the top row, every 3rd row is
            entirely green.
    Rule 3: For the non-red and non-green buttons, starting from the second-to-
            leftmost column, every 2nd column is entirely yellow.
    Rule 4: Any non-red, non-green, and non-yellow button is blue.

    :param n: No of circles in a row or column in the pattern
    :return: None
    """

    circleWidth = 40
    circleHeight = 40

    root = Tk()
    canvas = Canvas(root, width=n * circleWidth, height=n * circleHeight)
    canvas.pack()

    for row in range(n):
        for column in range(n):

            # Color strings via http://www.schemecolor.com/

            if (row + column) % 4 == 0:
                color = "red" #Red
            elif row % 3 == 0:
                color = rgbString(114, 201, 69) #Green
            elif column % 2 == 1:
                color = rgbString(255, 199, 24) #Yellow
            else:
                color = rgbString(68, 134, 244) #Blue

            left = 2 + column * circleWidth
            top = 2 + row * circleHeight
            right = left  + circleWidth
            bottom = top  + circleHeight

            drawButton(canvas, left, top, right, bottom, color)

    root.mainloop()

drawCirclePattern(10)
