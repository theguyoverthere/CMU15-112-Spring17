#******************************************************************************#
# Author: Tarique Anwer
# Date:   28/5/2017
# Description: Write the function isLatinSquare(a) that takes a 2d list and
#              returns True if it is a Latin square and False otherwise.
#              https://en.wikipedia.org/wiki/Latin_square
#******************************************************************************#

def isLatinSquare(a):
    """ Determine if the 2d list is a Latin Square.
    An n×n Latin square is a Latin rectangle with k=n. Specifically, a Latin
    square consists of n sets of the numbers 1 to n arranged in such a way that
    no orthogonal (row or column) contains the same number twice.

    For example, the two Latin squares of order two are given by
     [[1, 2],   [[2, 1],
       2, 1]]    [1, 2]]

    :param a: A 2d List
    :return: True if the 2d List is a Latin Square. False otherwise.
    """
    (rows, columns) = (len(a), len(a[0]))

    firstRow = a[0]
    for element in firstRow:
        if a.count(element) > 1:
            return False

    for row in range(1, rows):
        if sorted(a[row - 1]) != sorted(a[row]):
            return False

    return True
