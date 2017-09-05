def mostFrequent(L):
    # Return most frequent element in L, resolving ties arbitrarily.
    counts = dict()
    mostFrequentElement = None
    maxCount = 0

    for element in L:
        count = 1 + counts.get(element, 0)
        counts[element] = count

        if count > maxCount:
            maxCount = count
            mostFrequentElement = element

    return mostFrequentElement


def testMostFrequent():
    print("Testing mostFrequent()... ", end="")
    assert(mostFrequent([2,5,3,4,6,4,2,4,5]) == 4)
    assert(mostFrequent([2,3,4,3,5,3,6,3,7]) == 3)
    assert(mostFrequent([42]) == 42)
    assert(mostFrequent([]) == None)
    print("Passed!")

testMostFrequent()