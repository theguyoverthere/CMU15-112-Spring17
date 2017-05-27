def maxItemLength(a):
    maxLen = 0
    rows, columns = len(a), len(a[0])

    for row in range(rows):
        for column in range(columns):
            maxLen = max(maxLen, len(str(a[row][column])))

    return maxLen

def print2dList(a):

    if not a:
        print([])
        return

    rows, columns = len(a), len(a[0])
    fieldWidth = maxItemLength(a)

    print("[ ", end="")

    for row in range(rows):
        if row > 0:
            print("\n  ", end="")
        print("[ ", end="")

        for column in range(columns):
            if column > 0:
                print(", ", end="")

            formatSpec = "%" + str(fieldWidth) + "s"
            print(formatSpec % str(a[row][column]), end="")

        if row < rows - 1:
            print(" ],", end="")
        else:
            print(" ] ", end="")
    print("]")

a = [[1, 2, 3], [4, 5, 67]]
print2dList(a)
