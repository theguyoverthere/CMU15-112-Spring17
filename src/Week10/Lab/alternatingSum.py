#******************************************************************************#
# Author: Tarique Anwer
# Date:   16/2/2018
# Description: Write the function alternatingSum(L) that takes a possibly-empty
#              list of numbers, L, and returns their alternating sum, where
#              every other value is subtracted rather than added. For example:
#
#              alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 (that is, 3)
#              If L is empty, return 0.
#******************************************************************************#

def alternatingSum(L, depth=0):
    """ Takes a possibly-empty list of numbers, L and returns their alternating
    sum, where every other value is subtracted rather than added.

    :param L: Possibly empty, list of integers.
    :param depth: Only required for printing recursion stack, not as input.
    :return: Alternating sum of elements in the list.
    """

    # print(" " * depth, "alternatingSum(" + str(L) + ")")

    if len(L) == 0:
        result = 0
    elif len(L) == 1:
        result = L[0]
    else:
        result = L[0] - L[1] + alternatingSum(L[2:], depth + 1)

    # print(" " * depth, "..." + str(result))
    return result
