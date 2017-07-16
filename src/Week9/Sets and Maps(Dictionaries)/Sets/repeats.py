def repeats(L):
    # Returns a sorted list of the repeat elements in the list L
    seen = set()
    seenAgain = set()

    for element in L:
        if element in seen:
            seenAgain.add(element)
        seen.add(element)

    return sorted(seenAgain)

def _Repeats():
    print("Testing repeats()...", end="")
    assert(repeats([1,2,3,2,1]) == [1,2])
    assert(repeats([1,2,3,2,2,4]) == [2])
    assert(repeats(list(range(100))) == [ ])
    assert(repeats(list(range(100))*5) == list(range(100)))
    print("Passed!")

_Repeats()