#******************************************************************************#
# Author: Tarique Anwer
# Date:   13/5/2017
# Description: Write the function makeLetterTypePieChart that takes one required
#              parameter -- some text (which is just a string) -- and two
#              optional parameters, the winWidth and winHeight. The function
#              displays a window of the given size and fills it with a pie chart
#              that indicates the number of vowels, consonants, and other
#              characters in the text, with these constraints:
#              1. The fill color for vowels should be pink, consonants should be
#                 cyan, and others should be lightGreen.
#              2. Do not count whitespace characters at all. Hint: the isspace
#                 method can be handy here.
#              3. Draw the labels in 12-point Arial bold, formatted exactly as
#                 noted in the images below -- the letter type, and then in
#                 parentheses, the number of that letter type "of" the total
#                 number of non-whitespace characters, a comma, and then that
#                 ratio as an integer percentage.
#              4. Center the text in the center of the pie wedge.
#              5. The pink wedge (if it is present) must start at the vertical,
#                 followed counterclockwise by cyan, then lightGreen.
#              6. Do not draw a wedge if there are no characters of that type.
#              7. If all the characters are of a single type, draw a whole
#                 circle, with the label centered in the circle.
#              8. If there are no vowels, consonants, or other non-whitespace
#                 characters, then display "No data to display" centered in the
#                 window, in 20-point Arial bold.
#              9. The pie chart should fill 90% of the smaller of the window's
#                 width or height.
#              For example, this call: makeLetterTypePieChart("AB, c de!?!")
#              produces this result:
#              https://www.cs.cmu.edu/~112/notes/lab4.html
#******************************************************************************#
from tkinter import Tk, Canvas
import decimal
import math

def roundHalfUp(d):
    """ Round to nearest with ties going away from zero.
    :param d: Floating point number.
    :return: Rounded up integer
    """

    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def countVowelsAndConsonants(text):
    """ Count the number of vowels, consonants and other alphanumeric
        characters.

    :param text: A text string
    :return: A list with counts of vowels, consonants, other alphanumeric
             characters. The list is of the form:
             result[0] - Number of vowels in the string.
             result[1] - Number of consonants in the string.
             result[2] - Number of other alphanumeric characters in the string.
             result[3] - Total number of non-space characters in the string.
    """
    result = [0] * 4
    vowels = ["a", "e", "i", "o", "u"]

    for i in range(len(text)):

        if not text[i].isspace():
            if text[i].lower() in vowels:
                result[0] += 1 #Vowels
            elif text[i].isalpha():
                result[1] += 1 #Consonants
            else:
                result[2] += 1 #Others

    result[3] += result[0] + result[1] + result[2] #Total
    return result

def addTitle(canvas, xc, yc, title, font):
    """ Add title to canvas

    :param canvas: Canvas on which the title should be added.
    :param xc: x-coordinate of the centre of canvas
    :param yc: y-coordinate of the centre of canvas
    :param title: Text to be displayed
    :param font: Text font
    :return: None
    """
    canvas.create_text(xc, yc, text=title, font=font)

def drawCircle(canvas, x0, y0, x1, y1, color):
    """ Draw a circle in the area bounded by (x0,y0) in the top-left and
       (x1,y1) at the bottom-right

    Given the top-left and bottom-right rectangle coordinate, the function
    draws a circle on the canvas.

    :param canvas: Canvas on which the graphics will be displayed.
    :param x0: Top left corner x-coordinate
    :param y0: Top left corner y-coordinate
    :param x1: Bottom right corner x-coordinate
    :param y1: Bottom right corner y-coordinate
    :param color: Fill color of the circle
    :return: None
    """

    # Calculate the parameters for drawing the clock

    width = x1 - x0
    height = y1 - y0
    r = min(width, height) / 2
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2

    # Draw the circle
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color)

def drawArc(canvas, left, top, right, bottom, color, startAngle, extentAngle):
    """ Draw an arc in the area bounded by (x0,y0) in the top-left and
       (x1,y1) at the bottom-right

    Given the top-left and bottom-right rectangle coordinate, the function
    draws aan arc on the canvas.

    :param canvas: Canvas on which the graphics will be displayed.
    :param left: Top left corner x-coordinate
    :param top: Top left corner y-coordinate
    :param right: Bottom right corner x-coordinate
    :param bottom: Bottom right corner y-coordinate
    :param color: Fill color of the arc
    :param startAngle: Start Angle of the arc in degrees.
    :param extentAngle: Angle from the start angle to the end angle
    :return: None
    """

    canvas.create_arc(left, top, right, bottom,
                      start=startAngle, extent=extentAngle, fill=color)

def drawPieChart(canvas, left, top, right, bottom, counts, percentSize):
    """ Draw a pie chart of vowels, consonants and other characters.

    :param canvas: Canvas on which the graphics will be displayed.
    :param left: Top left corner x-coordinate
    :param top: Top left corner y-coordinate
    :param right: Bottom right corner x-coordinate
    :param bottom: Bottom right corner y-coordinate
    :param counts: List consisting of counts of vowels, consonants and other
           characters obtained from the function countVowelsAndConsonants(text)
    :param percentSize: Percentage size of the window occupied by the pie
           chart
    :return: None
    """

    #Psuedo-enum
    vowels, consonant, others, total = range(4)

    #A string of spaces of a null string
    if counts[total] == 0:
        cx = (left + right) / 2
        cy = (top + bottom) / 2
        text = "No data to display"
        font = "Arial 16 bold"

        addTitle(canvas, cx, cy, text, font)
    else:
        percents = [0] * 3
        startAngle = 90

        for i in range(len(counts) - 1):
            percents[i] = counts[i] / counts[total]

            if i == vowels:
                color = "pink"
            elif i == consonant:
                color = "cyan"
            else:
                color = "lightGreen"

            cx = (left + right) / 2
            cy = (top + bottom) / 2
            font = "Arial 12 bold"
            text = ("vowels (" + str(counts[i]) + " of " +
                    str(counts[total]) + ", " +
                    str(roundHalfUp(percents[i] * 100)) + "%)")

            if percents[i] == 1:
                # Draw a full circle, because drawing an arc of 360 degrees
                # will not fill the circle with color.
                drawCircle(canvas, left, top, right, bottom, color)

                # Add text label.
                addTitle(canvas, cx, cy, text, font)
                break
            else:
                if percents[i] > 0:
                    # Draw the arc.
                    extentAngle = percents[i] * 360
                    drawArc(canvas, left, top, right, bottom, color,
                            startAngle, extentAngle)

                    # Add text label.
                    width = (right - left) / percentSize
                    height = (bottom - top) / percentSize

                    cx = width / 2
                    cy = height / 2
                    textRadius = min(width, height) / 4
                    radians = (math.pi / 180) * (startAngle + (extentAngle / 2))

                    textX = cx + textRadius * math.cos(radians)
                    textY = cy - textRadius * math.sin(radians)

                    addTitle(canvas, textX, textY, text, font)

                    startAngle += extentAngle


def makeLetterTypePieChart(text, winWidth=500, winHeight=500):
    """
    The function makeLetterTypePieChart takes one required parameter -- some
    text (which is just a string) -- and two optional parameters, the winWidth
    and winHeight.
    The function displays a window of the given size and fills it with a pie
    chart that indicates the number of vowels, consonants, and other characters
    in the text, with these constraints:

    1. The fill color for vowels is pink, consonants is cyan, and others is
       lightGreen.
    2. Whitespace characters aren't counted at all.
    3. The labels are drawn in 12-point Arial bold, formatted exactly as noted
       in the images below -- the letter type, and then in parentheses, the
       number of that letter type "of" the total number of non-whitespace
       characters, a comma, and then that ratio as an integer percentage.
    4. The text is centered in the center of the pie wedge.
    5. The pink wedge (if it is present) starts at the vertical, followed
       counterclockwise by cyan, then lightGreen.
    6. If there are no characters of a type, its corresponding wedge is not
       drawn.
    7. If all the characters are of a single type, a whole circle is drawn, with
       the label centered in the circle.
    8. If there are no vowels, consonants, or other non-whitespace characters,
       then "No data to display" is displayed at the center in the window,
       in 20-point Arial bold.
    9. The pie chart fills 90% of the smaller of the window's width or height.

    For example, this call: makeLetterTypePieChart("AB, c de!?!") produces this
    result: https://www.cs.cmu.edu/~112/notes/lab4.html

    :param text: A string of text
    :param winWidth: Width of the window (optional)
    :param winHeight: Height of the window (optional)
    :return: None
    """

    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    cx = winWidth / 2
    cy = winHeight / 2
    percentSize = 0.90

    delta = (percentSize * min(winWidth, winHeight)) / 2

    left = cx - delta
    top = cy - delta
    right = cx + delta
    bottom = cy + delta

    counts = countVowelsAndConsonants(text)
    drawPieChart(canvas, left, top, right, bottom, counts, percentSize)

    root.mainloop()

# makeLetterTypePieChart("AB, c de!?!", 500, 500)
# makeLetterTypePieChart("AB e")
# makeLetterTypePieChart("A")
# makeLetterTypePieChart(" ")
