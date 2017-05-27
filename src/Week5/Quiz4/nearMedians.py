
def validList(L):
    if not L: return False
    for num in L:
        if not isinstance(num, int): return False

    return True

def nearMedians(L):
    result = []

    if validList(L):
        sortedList = sorted(L)

        if len(sortedList) % 2 == 1:
            median = sortedList[len(sortedList) // 2]
        else:
            median = (sortedList[int(len(sortedList) / 2) - 1] +
                      sortedList[int(len(sortedList) / 2)]) / 2

        for value in sortedList:
            if abs(value - median) <= 10:
                result.append(value)

        return result

    return None


def testNearMedians():
    print('Testing nearMedians()...', end='')
    assert(nearMedians([1, 49, 50, 51, 99]) == [49, 50, 51])
    assert(nearMedians([49, 1, 50, 99, 51]) == [49, 50, 51])
    assert(nearMedians([1, 48, 52, 99]) == [48, 52])
    assert(nearMedians([48, 1, 99, 52]) == [48, 52])
    assert(nearMedians([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1])
    assert(nearMedians([ ]) == None)
    assert(nearMedians(["ugh"]) == None)
    assert(nearMedians("ugh") == None)
    print('Passed')

testNearMedians()