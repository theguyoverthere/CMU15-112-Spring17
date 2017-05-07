#******************************************************************************#
# Author: Tarique Anwer
# Date:   7/5/2017
# Description: First, read about look-and-say numbers on Wikipedia. Then, write
#              the function lookAndSay(a) that takes a list of numbers and
#              returns a list of numbers that results from "reading off" the
#              initial list using the look-and-say method, using tuples for each
#              (count, value) pair. For example:
#              lookAndSay([]) == []
#              lookAndSay([1,1,1]) == [(3,1)]
#              lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
#              lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
#******************************************************************************#
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
