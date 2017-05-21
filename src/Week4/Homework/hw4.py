#################################################
# Hw4
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

# The Second Edition of the 20-volume Oxford English Dictionary contains full
# entries for 171,476 words in current use, and 47,156 obsolete words. To this
# may be added around 9,500 derivative words included as subentries.
# That's roughly, 2,28,000 words. A 9 letter word would produce 9! = 3,62,880
# combinations. If we go down the permutation route, we're looking at a
# nightmare!

def letterCounts(s):
    """
    Form a list with the count of letters present in the string s. The list is
    26 characters long, and represents the count of each of the letter present
    in the English alphabet.

    :param s: A string of characters.
    :return: A list with the count of letters in the string.

    """
    counts = [0] * 26

    for ch in s.upper():
        if (ch >= "A") and (ch <= "Z"):
            counts[ord(ch) - ord("A")] += 1

    return counts

def possibleToFormWord(word, hand):
    """
    Check to see if it is possible to form the word, with the characters
    available in the string "hand"

    :param word: A string, which is supposedly a valid word.
    :param hand: A string of lower-case characters
    :return: True if it is possible to form the word given with all or some of
           the letters available in the string "hand".
    """

    letterCountWord = letterCounts(word)
    letterCountHand = letterCounts(hand)

    for i in range(len(letterCountWord)):
        if letterCountWord[i] > letterCountHand[i]:
            return False

    return True

def computeWordScore(word, letterScores):
    """ Compute the word score.

    :param word: A string whose score needs to be computed.
    :param letterScores: A list of scores for each lowercase letter of the
           English alphabet.
    :return: Score as a positive integer.
    """
    score = 0

    for c in word:
        score += letterScores[ord(c) - ord('a')]

    return score

def bestScrabbleScore(dictionary, letterScores, hand):
    """
    bestScrabbleScore(dictionary, letterScores, hand) takes 3 lists --
    dictionary (a list of lowercase words), letterScores(a list of 26 integers),
    and hand (a list of lowercase characters) and returns a tuple of the
    highest-scoring word in the dictionary that can be formed by some
    arrangement of some subset of letters in the hand, followed by its score. In
    the case of a tie, the first element of the tuple is instead a list
    of all such words in the order they appear in the dictionary. If no such
    words exist, the function returns None.

    :param dictionary: A list of string elements, considered to be valid words.
    :param letterScores: A list of positive integers, representing scores of
           each lowercase letter of the English alphabet.
    :param hand: A list of characters available to form a valid word.
    :return: List of word(s) with the highest score, or None. If more than
           two words in the dictionary result in the same score, the words are
           returned as a list themselves.

           For example, the following returns are valid:
           a) ["Hello", "lloeH", 16]
           b) ["good", 10]
           c None
    """
    result = []
    possibleWords = []
    highestScore = 0

    for word in dictionary:
        if possibleToFormWord(word, "".join(hand)):
            score = computeWordScore(word, letterScores)

            if score >= highestScore:
                if score > highestScore:
                    possibleWords.clear()

                possibleWords.append(word)
                highestScore = score

    if not possibleWords:
        return None
    else:
        if len(possibleWords) > 1:
            result.append(possibleWords)
        else:
            result.append("".join(possibleWords))

        result.append(highestScore)
        return tuple(result)


###### Autograded Bonus ########
# (place non-autograded bonus below #ignore-rest line!) #

def runSimpleProgram(program, args):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
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


def testRunSimpleTortoiseProgram1():
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

def testRunSimpleTortoiseProgram2():
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

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

#################################################
# Test Functions
#################################################

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testRunSimpleTortoiseProgram()
    testBestScrabbleScore()
    # testRunSimpleProgram()

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
