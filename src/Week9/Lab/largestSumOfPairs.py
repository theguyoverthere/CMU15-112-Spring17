#******************************************************************************#
# Author: Tarique Anwer
# Date:   30/7/2017
# Description: Write the function largestSumOfPairs(a) that takes a list of
#              integers, and returns the largest sum of any two elements in that
#              list, or None if the list is of size 1 or smaller. So,
#              largestSumOfPairs([8,4,2,8]) returns the largest of (8+4), (8+2),
#              (8+8), (4+2), (4+8), and (2+8), or 16.  The naive solution is to
#              try every possible pair of numbers in the list.
#              This runs in O(n**2) time and is much too slow.
#******************************************************************************#

def largestSumOfPairs(a):
    """ Takes a list of integers, and returns the largest sum of any two
    elements in that list, or None if the list is of size 1 or smaller.

    :param a: Unsorted list of integers
    :return: The largest sum of any two elements in the list, or None if the
             list is of size 1 or smaller.
    """
    if len(a) < 2:
        return None
    else:
        a.sort()
        return a[len(a) - 1] + a[len(a) - 2]
