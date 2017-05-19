#******************************************************************************#
# Author: Tarique Anwer
# Date:   15/5/2017
# Description: In addition to the Tkinter which we all know and love, Python
#              usually comes with another graphics package called "Turtle
#              Graphics", which you can read about here. We will definitely not
#              be using turtle graphics in this problem (and you may not do so
#              in your solution!), but we will instead implement a small
#              turtle-like (or maybe turtle-inspired) graphics language of our
#              own. We'll call it Tortoise Graphics.
#
#              - https://docs.python.org/2/library/turtle.html
#
#              First, we need to understand how Tortoise Graphics programs work.
#              Your tortoise starts in the middle of the screen, heading to the
#              right. You can direct your tortoise with the following commands:
#
#              color name - Set the drawing color to the given name, which is
#                           entered without quotes, and which can be "red",
#                           "blue", "green", or any other color that Tkinter
#                           understands. It can also be "none", meaning to not
#                           draw.
#              move n - Move n pixels straight ahead, where n is a non-negative
#                       integer, while drawing a 4-pixel-wide line in the
#                       current drawing color. If the drawing color is "none",
#                       just move straight ahead without drawing (that is, just
#                       change the tortoise's location).
#              left n - Turn n degrees to the left, without moving, where n is a
#                       non-negative integer.
#              right n - Turn n degrees to the right, without moving, where n is
#                       a non-negative integer.
#
#              Commands are given one-per-line. Lines can also contain comments,
#              denoted by the hash sign (#), and everything from there to the
#              end-of-line is ignored. Blank lines and lines containing only
#              whitespace and/or comments are also ignored.
#
#              With this in mind, write the function
#              runSimpleTortoiseProgram(program, winWidth=500, winHeight=500)
#              that takes a program as specified above and runs it, displaying a
#              window (which is 500x500 by default) with the resulting drawing
#              from running that program. Your function should also display the
#              tortoise program in that window, in a 10-point font, in gray
#              text, running down the left-hand side of the window (say 10
#              pixels from the left edge).
#
#              Don't worry if the program is longer than can fit in the window
#              (no need to scroll or otherwise deal with this). Also, you are
#              not responsible for any syntax errors or runtime errors in the
#              tortoise program.
#
#              For example, this call:
#              runSimpleTortoiseProgram("""
#              #  This is a simple tortoise program
#              color blue
#              move 50
#
#              left 90
#
#              color red
#              move 100
#
#              color none # turns off drawing
#              move 50
#
#              right 45
#
#              color green # drawing is on again
#              move 50
#
#              right 45
#
#              color orange
#              move 50
#
#              right 90
#
#              color purple
#              move 100
#              """, 300, 400) produces this result in a 300x400 window:
#              https://www.cs.cmu.edu/~112/notes/hw4.html
#******************************************************************************#
from tkinter import Tk, Canvas, W
import math

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    """
    In addition to the Tkinter, Python usually comes with another graphics
    package called "Turtle Graphics". We will not be using turtle graphics in
    this problem but we will instead implement a small turtle-like (or maybe
    turtle-inspired) graphics language of our own. We'll call it Tortoise
    Graphics.

    First, we need to understand how Tortoise Graphics programs work.
    The tortoise starts in the middle of the screen, heading to the right. It
    can be directed with the following commands:

    color name - Set the drawing color to the given name, which is entered
                 without quotes, and which can be "red", "blue", "green", or any
                 other color that Tkinter understands. It can also be "none",
                 meaning to not draw.
    move n - Move n pixels straight ahead, where n is a non-negative integer,
             while drawing a 4-pixel-wide line in the current drawing color.
             If the drawing color is "none", just move straight ahead without
             drawing (that is, just change the tortoise's location).
    left n - Turn n degrees to the left, without moving, where n is a non-
             negative integer.
    right n - Turn n degrees to the right, without moving, where n is a
             non-negative integer.

    Commands are given one-per-line. Lines can also contain comments, denoted by
    the hash sign (#), and everything from there to the end-of-line is ignored.
    Blank lines and lines containing only whitespace and/or comments are also
    ignored.

    runSimpleTortoiseProgram(program, winWidth=500, winHeight=500)takes a
    program as specified above and runs it, displaying a window (which is
    500x500 by default) with the resulting drawing from running that program.

    The function also displays the tortoise program in that window, in a
    10-point font, in gray text, running down the left-hand side of the window
    (say 10 pixels from the left edge).

    See https://www.cs.cmu.edu/~112/notes/hw4.html for an example.

    :param program: The tortoise program which needs to be executed. Essentially
        consists of a series of statements arranged in a string.
    :param winWidth: Canvas width
    :param winHeight: Canvas height
    :return: None
    """

    angle = 0
    lineWidth = 4

    # Text Display parameters
    x0 = 10 #Margin
    y0 = 0
    textHeight = 10

    #Initial location of the Tortoise
    xTortoise = winWidth / 2
    yTortoise = winHeight / 2

    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    for statement in program.splitlines():
        y0 += textHeight

        # Add the statement to the canvas
        canvas.create_text(x0, y0, text=statement,
                           font="Helvetica 7", anchor=W, fill="gray")

        # Draw the tortoise
        if not (statement.strip() == "" or statement.strip().startswith("#")):
            operator = statement.split(" ")[0]
            operand = statement.split(" ")[1]

            if operator == "color":
                color = operand
            elif operator == "left":
                angle += int(operand) * math.pi / 180
            elif operator == "right":
                angle -= int(operand) * math.pi / 180
            elif operator == "move":
                pixels = int(operand)

                xTortoiseEnd = xTortoise + pixels * math.cos(angle)
                yTortoiseEnd = yTortoise - pixels * math.sin(angle)

                if color != "none":
                    canvas.create_line(xTortoise, yTortoise,
                                       xTortoiseEnd, yTortoiseEnd,
                                       fill=color,
                                       width=lineWidth)
                xTortoise = xTortoiseEnd
                yTortoise = yTortoiseEnd

    root.mainloop()

runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")
