def isPermutation(L):
    # returns True if L is a permutation of [0, ...., n-1]
    # and False otherwise

    return set(L) == set(range(len(L)))

def testIsPermutation():
    print("Testing isPermutation()...", end="")
    assert(isPermutation([0,2,1,4,3]) == True)
    assert(isPermutation([1,3,0,4,2]) == True)
    assert(isPermutation([1,3,5,4,2]) == False)
    assert(isPermutation([1,4,0,4,2]) == False)
    print("Passed!")

testIsPermutation()