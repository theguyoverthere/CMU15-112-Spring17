#******************************************************************************#
# Author: Tarique Anwer
# Date:   9/5/2017
# Description: Background: a cryptarithm is a puzzle where we start with a
#              simple arithmetic statement but then we replace all the digits
#              with letters (where the same digit is replaced by the same letter
#              each time). We will limit such puzzles to strings the form
#              "A+B=C" (no spaces), where A, B, and C are positive integers.
#              For example, "SEND+MORE=MONEY" is such a puzzle. The goal of the
#              puzzle is to find an assignment of digits to the letters to make
#              the math work out properly. For example, if we assign 0 to "O", 1
#              to "M", 2 to "Y", 5 to "E", 6 to "N", 7 to "D", 8 to "R", and 9
#              to "S" we get:
#                S E N D       9 5 6 7
#              + M O R E     + 1 0 8 5
#              ---------     ---------
#              M O N E Y     1 0 6 5 2
#              And so we see that this assignment does in fact solve the
#              problem! Now, we need a way to encode a possible solution. For
#              that, we will use a single string where the index of the letter
#              corresponds to the digit it represents. Thus, the string
#              "OMY--ENDRS" represents the assignments listed above (the dashes
#              are for unassigned digits). With this in mind, write the function
#              solvesCryptarithm(puzzle, solution) that takes two strings, a
#              puzzle (such as "SEND+MORE=MONEY") and a proposed solution (such
#              as "OMY--ENDRS"). Your function should return True if
#              substituting the digits from the solution back into the puzzle
#              results in a mathematically correct addition problem, and False
#              otherwise. You do not have to check whether a letter occurs more
#              than once in the proposed solution, but you do have to verify
#              that all the letters in the puzzle occur somewhere in the
#              solution (of course). You may not use the eval() function. Also,
#              you almost surely will want to write at least one well-chosen
#              helper function.
#******************************************************************************#
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
