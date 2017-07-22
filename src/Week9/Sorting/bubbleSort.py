#******************************************************************************#
# Author: Tarique Anwer
# Date:   18/7/2017
# Description: Bubble sort is a simple sorting algorithm that repeatedly steps
#              through the list to be sorted, compares each pair of adjacent
#              items and swaps them if they are in the wrong order. The pass
#              through the list is repeated until no swaps are needed, which
#              indicates that the list is sorted. The algorithm, which is a
#              comparison sort, is named for the way smaller or larger elements
#              "bubble" to the top of the list.
#******************************************************************************#

def swap(L, i, j):
    """ Swap two elements in a list.

    :param L: A list whose elements need to be swapped.
    :param i: Index 1 of the elements which needs to be swapped.
    :param j: Index 2 of the elements which needs to be swapped.
    :return: None
    """

    L[i], L[j] = L[j], L[i]

def bubbleSort(L):
    """ Bubble sort is a simple sorting algorithm that repeatedly steps through
    the list to be sorted, compares each pair of adjacent items and swaps them
    if they are in the wrong order. The pass through the list is repeated until
    no swaps are needed, which indicates that the list is sorted. The algorithm,
    which is a comparison sort, is named for the way smaller or larger elements
    "bubble" to the top of the list.

    :param L: Unsorted list of integers
    :return: Sorted list of integers.
    """
    for i in range(len(L)):
        for j in range(1, len(L) - i):
            if L[j] < L[j - 1]:
                swap(L, j, j - 1)
    return L
