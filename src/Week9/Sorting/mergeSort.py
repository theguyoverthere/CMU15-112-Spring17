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

def mergeLists(M, startL, endL, startR, endR):
    """ Merge two sorted lists into a larger sorted list.

    :param M: The original list which needs to be sorted in-place.
    :param startL: Start index of the left sub-list.
    :param endL: End index of the left sub-list.
    :param startR: Start index of the right sub-list.
    :param endR: End index of the right sub-list.
    :return: None
    """

    a = M[startL: endL + 1]
    b = M[startR: endR + 1]

    indexA = 0
    indexB = 0
    indexR = 0
    result = [None] * (len(a) + len(b))

    for i in range(len(result)):
        if indexA <= len(a) - 1 and indexB <= len(b) - 1:
            if a[indexA] < b[indexB]:
                result[indexR] = a[indexA]
                indexA += 1
            else:
                result[indexR] = b[indexB]
                indexB += 1
        elif indexA == len(a):
            result[indexR] = b[indexB]
            indexB += 1
        else:
            result[indexR] = a[indexA]
            indexA += 1

        indexR += 1

    for i in range(len(result)):
        M[startL + i] = result[i]


def mergeSort(L):
    """ Merge Sort sorts an n-element list by repeatedly merging sorted
    sub-sequences of elements in-place.

    Consider an n-element list L = [n1, n2, n3, n4, ...., nn] which needs to be
    sorted.

    The n-element list is divided into n lists consisting of a single element.

                         [n1], [n2], [n3], ..., [nn]

    Since each list consists of only one element, all of them start sorted. In
    the next pass, two consecutive 1-element lists are merged together into a
    sorted list of two element each.

                     [n2, n1], [n3, n4], .... [nn, n(n -1)]

    In the next pass, two consecutive 2-element lists are merged together into a
    sorted list of four element each.

                [n2, n3, n1, n4], .... [n(n-3), n(n-2), nn, n(n -1)]

    This process is repeated until the list is completely sorted.

    :param L: An unsorted list of integers.
    :return: Sorted list of integers.
    """

    partitionSize = 1

    while partitionSize < len(L):
        count = 0
        startL = 0
        mergeCount = int((len(L) // 2) / partitionSize)

        # For each partitionSize, adjacent sub-lists are merged mergeCount
        # number of times.
        while count < mergeCount:
            endL = startL + partitionSize - 1
            startR = endL + 1
            endR = min(startR + partitionSize - 1, len(L) - 1)

            mergeLists(L, startL, endL, startR, endR)
            startL = endR + 1
            count += 1

        partitionSize *= 2

    return L
