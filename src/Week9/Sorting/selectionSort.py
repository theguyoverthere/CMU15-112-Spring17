#******************************************************************************#
# Author: Tarique Anwer
# Date:   18/7/2017
# Description: Selection Sort sorts n numbers stored in a list L by repeatedly
#              finding the smallest element of L and exchanging it with the
#              first unsorted element in the list.
#
#              Therefore, the minimum element in the list is exchanged with the
#              element present at L[0], the second minimum value with the
#              element at L[1] and so forth, until the list is completed sorted.
#******************************************************************************#

def locateMinimum(L, start, end):
    """ Locate the minimum element in a list between the indices 'start' and
    'end'.

    :param L: A List of integers
    :param start: Index at which the search for minimum element should begin.
    :param end:  Index at which the search for minimum element should end.
    :return: None
    """
    minIndex = start

    for i in range(start, end + 1):
        if L[i] < L[minIndex]:
            minIndex = i

    return minIndex

def swap(L, i, j):
    """ Swap two elements in a list.

    :param L: A list whose elements need to be swapped.
    :param i: Index 1 of the elements which needs to be swapped.
    :param j: Index 2 of the elements which needs to be swapped.
    :return: None
    """

    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def selectionSort(L):
    """ Selection Sort sorts n numbers stored in a list L by repeatedly finding
    the smallest element of L and exchanging it with the first unsorted element
    in the list.

    The minimum element in the list is exchanged with the element present at
    L[0], the second minimum value with the element at L[1] and so forth, until
    the list is completed sorted.

    :param L: List of unsorted integers
    :return: List of sorted integers
    """

    for start in range(len(L)):
        index = locateMinimum(L, start, len(L) - 1)
        swap(L, index, start)

    return L
