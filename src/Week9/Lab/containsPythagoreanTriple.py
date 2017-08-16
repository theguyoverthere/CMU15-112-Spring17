def binarySearch(a, x):
    lower = 0
    upper = len(a) - 1
    a.sort()

    while upper - lower >= 0:
        middle = (upper + lower) // 2

        if a[middle] == x:
            return True
        elif x > a[middle]:
            lower = middle + 1
        else:
            upper = middle - 1

    return False

def containsPythagoreanTriple(a):
    squares = [element ** 2 for element in a]
    pairSums = []

    for i in range(len(squares)):
        for j in range(len(squares)):
            if i != j:
                pairSums.append(squares[i] + squares[j])

    for p in range(len(pairSums)):
        if binarySearch(squares, pairSums[p]):
            return True

    return False