#################################################
# Lab4
#################################################

import cs112_s17_linter
import math, string, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Problems
#################################################

#-----------------------------------------------#
# lookAndSay(a)                                 #
#-----------------------------------------------#

def lookAndSay(a):
    """ Look and Say!
    Takes a list of numbers that result from "reading off" the initial list
    using the look-and-say method, using tuples for each (count, value) pair.

    For example:
    lookAndSay([]) == []
    lookAndSay([1,1,1]) == [(3,1)]
    lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
    lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]

    :param a: List of integers.
    :return: List of tuples consisting of the (count, value) pairs.
    """

    # Check for empty list!
    if not a: return []

    i = 0
    result = []
    currentPair = [1, 0]

    while True:
        currentPair[1] = a[i]

        if i == len(a) - 1:
            result.append(tuple(currentPair))
            break
        elif a[i] == a[i + 1]:
            currentPair[0] += 1
        else:
            result.append(tuple(currentPair))
            currentPair[0] = 1
        i += 1

    return result

#-----------------------------------------------#
# inverseLookAndSay(a)                          #
#-----------------------------------------------#

def inverseLookAndSay(a):
    """ Inverse of the lookAndSay function coded above.

    Takes a list of tuples, where each tuple consists of a (count, value) pair
    and converts it to a list of integers. For example,

    inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]

    :param a: List of tuples consisting of (count, value) pair.
    :return: List of integers.
    """

    if not a:
        return [] # Check for empty list!

    result = []
    for i in range(len(a)):
        for j in range(a[i][0]):
            result.append(a[i][1])

    return result

#-----------------------------------------------#
# solvesCryptarithm                             #
#-----------------------------------------------#

def getNumericArgument(arg, solution):
    """ Return the numeric representation of the encoded string argument.

    :param arg: A String representation of the one of the arguments of the
                addition problem.
    :param solution: A single string where the index of the letter corresponds
                   to the digit it represents. Thus, the string "OMY-ENDRS"
                   represents the assignment:
                   "O" - 0   "N" - 5
                   "M" - 1   "D" - 6
                   "Y" - 2   "R" - 7
                   "E" - 4   "S" - 8
    :return: A integral representation of the argument.
    """
    result = []

    for i in range(len(arg)):
        index = solution.find(arg[i])
        if index != -1:
            result.append(str(index))

    if "".join(result) == "":
        return -1
    else:
        return int("".join(result) )

def isLegalSolution(puzzle, solution):
    """ Check if the solution is legal.

    The function ensures that all the letters in the puzzle occur somewhere in
    the solution.

    :param puzzle: A string of the form "A+B=C", where A, B and C all happen to
                   be positive integers. The integers are obtained by
                   substituting the index of the letter in the solution.
    :param solution: A single string where the index of the letter corresponds
                   to the digit it represents. Thus, the string "OMY-ENDRS"
                   represents the assignment:
                   "O" - 0   "N" - 5
                   "M" - 1   "D" - 6
                   "Y" - 2   "R" - 7
                   "E" - 4   "S" - 8
    :return: Returns True is all the letters in the puzzle occur somewhere in
             the solution. False otherwise.
    """

    for i in range(len(puzzle)):
        if puzzle[i].isalpha() and solution.find(puzzle[i]) == -1:
            return False

    return True

def solvesCryptarithm(puzzle, solution):
    """ Verify that the solution for Cryptarithm is correct.

    A cryptarithm is a puzzle where we start with a simple arithmetic statement
    but then we replace all the digits with letters (where the same digit is
    replaced by the same letter each time). We will limit such puzzles to
    strings the form "A+B=C" (no spaces), where A, B, and C are positive
    integers.
    For example, "SEND+MORE=MONEY" is such a puzzle. The goal of the puzzle is
    to find an assignment of digits to the letters to make the math work out
    properly. For example, if we assign 0 to "O", 1 to "M", 2 to "Y", 5 to "E",
    6 to "N", 7 to "D", 8 to "R", and 9 to "S" we get:
      S E N D       9 5 6 7
    + M O R E     + 1 0 8 5
    ---------     ---------
    M O N E Y     1 0 6 5 2

    We see that this assignment does in fact solve the problem! To encode a
    possible solution, we will use a single string where the index of the letter
    corresponds to the digit it represents. Thus, the string "OMY--ENDRS"
    represents the assignments listed above (the dashes are for unassigned
    digits).

    The function solvesCryptarithm(puzzle, solution) that takes two strings, a
    puzzle (such as "SEND+MORE=MONEY") and a proposed solution (such as
    "OMY--ENDRS"). It returns True if substituting the digits from the solution
    back into the puzzle results in a mathematically correct addition problem,
    and False otherwise.

    :param puzzle: A string of the form "A+B=C", where A, B and C all happen to
                   be positive integers. The integers are obtained by
                   substituting the index of the letter in the solution.
    :param solution: A single string where the index of the letter corresponds
                   to the digit it represents. Thus, the string "OMY-ENDRS"
                   represents the assignment:
                   "O" - 0   "N" - 5
                   "M" - 1   "D" - 6
                   "Y" - 2   "R" - 7
                   "E" - 4   "S" - 8
    :return: A boolean stating whether the given solution solves the addition
             problem represented in the puzzle.
    """

    if isLegalSolution(puzzle, solution):
        argA = getNumericArgument(puzzle[: puzzle.find("+")], solution)
        argB = getNumericArgument(puzzle[puzzle.index("+") : puzzle.find("=")],
                                  solution)
        result = getNumericArgument(puzzle[puzzle.find("="):], solution)

        return argA + argB == result

    return False


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

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

def testMakeLetterTypePieChart():
    print("Testing makeLetterTypePieChart()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    makeLetterTypePieChart("AB, c de!?!")
    makeLetterTypePieChart("AB e")
    makeLetterTypePieChart("A")
    makeLetterTypePieChart("               ")
    print("Done!")

#################################################
# Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolvesCryptarithm()
    testMakeLetterTypePieChart()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,del,is,pass,repr' +
        'as,class,except,finally,global,lambda,nonlocal,raise,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len,'+
        #'ascii,bin,dir,enumerate,format,help,hex,id,iter,'+
        #'list,oct,slice,sorted,tuple,zip,'+
        '__import__,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,' +
        'eval,exec,filter,frozenset,getattr,globals,' +
        'hasattr,hash,issubclass,' +
        'locals,map,memoryview,next,object,open,property,set,' +
        'setattr,staticmethod,super,' +
        'type,vars,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
