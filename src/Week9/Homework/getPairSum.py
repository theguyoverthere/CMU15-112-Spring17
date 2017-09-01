#******************************************************************************#
# Author: Tarique Anwer
# Date:   22/8/2017
# Description: Write the function getPairSum(a, target) that takes a list of
#              numbers and a target value (also a number), and if there is a
#              pair of numbers in the given list that add up to the given target
#              number, returns that pair, and otherwise returns an empty list.
#
#              If there is more than one valid pair, you can return any of them.
#              You should write two different versions, one that runs in O(n**2)
#              and the other in O(n). For example:
#
#              getPairSum([1],1) == []
#              getPairSum([5,2],7) in [ [5,2], [2,5] ]
#              getPairSum([10,-1,1,-8,3,1], 2) in [ [10,-8], [-8,10] ]
#              (can also return [-1,3] or [1,1])
#              getPairSum([10,-1,1,-8,3,1],10) == []
#******************************************************************************#
def getPairSum(a, target):
    """
    Takes a list of numbers and a target value(also a number), and if there is a
    pair of numbers in the given list that add up to the given target number,
    returns that pair, and otherwise returns an empty list.

    :param a: A list of numbers.
    :param target: A target value which is equal to the sum of two numbers in
                   the list. Such a pair may or may not exist though.
    :return: The pair of numbers whose sum equals the target value.
    """
    d = dict()
    result = []
    pairExists = False

    # Construct a dictionary
    for element in a:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1

    for element in d:
        # If the target value is twice the current element, make sure there
        # exists another instance of the element in the list to pair up with.
        if target == 2 * element:
            if d[element] > 1:
                pairExists = True
                break
        elif (target - element) in d:
            pairExists = True
            break

    if pairExists:
        result.append(element)
        result.append(target - element)

    return result