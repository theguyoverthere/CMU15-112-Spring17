#******************************************************************************#
# Author: Tarique Anwer
# Date:   1/6/2017
# Description: Write removeRowAndCol non-destructively and also destructively,
#              as described here:
#              1. Write the function removeRowAndCol(A, row, col) that takes a
#              2d list A, a row index and a col index, and non-destructively
#              returns a new 2d list with the given row and column removed.
#              So if: A = [ [ 2, 3, 4, 5],
#                           [ 8, 7, 6, 5],
#                           [ 0, 1, 2, 3]
#                         ]
#              Then removeRowAndCol(A, 1, 2) returns:
#                         [ [ 2, 3, 5],
#                           [ 0, 1, 3]
#                         ]
#              You may assume the row and col are legal, in that they are
#              non-negative integers no larger than the largest row and col
#              index, respectively. Also, A remains unchanged.
#
#              2. destructiveRemoveRowAndCol(A, row, col)
#              Rewrite the previous function so it is destructive. In this case,
#              the return value is None and instead the 2d list A is
#              destructively modified to remove the given row and column.
#******************************************************************************#

def removeRowAndCol(A, row, col):
    """ Remove the specified row and column, without modifying the original
    list.

    removeRowAndCol(A, row, col) takes a 2d list A, a row index and a col index,
    and non-destructively returns a new 2d list with the given row and column
    removed.

    So if: A = [ [ 2, 3, 4, 5],
                 [ 8, 7, 6, 5],
                 [ 0, 1, 2, 3]
               ]
    Then removeRowAndCol(A, 1, 2) returns:
                 [ [ 2, 3, 5],
                   [ 0, 1, 3]
                 ]
    It is assumed that the row and col values are legal, in that they are
    non-negative integers no larger than the largest row and col index,
    respectively. Also, A remains unchanged.

    :param A: A 2d List
    :param row: Row to be removed from the 2d List. Must be a legal value.
    :param col: Column to be removed from the 2d List. Must be a legal value.
    :return: A 2d List with the specified row and column removed.
    """

    result = []
    (rows, columns) = (len(A), len(A[0]))

    for i in range(rows):
        if i != row:
            subList =[]
            for j in range(columns):
                if j != col:
                    subList.append(A[i][j])
            result.append(subList)

    return result
