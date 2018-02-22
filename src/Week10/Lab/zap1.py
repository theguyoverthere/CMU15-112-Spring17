def zap1(L, M):
    if len(L) == 1 or len(M) == 1:
        return [(L[0], M[0])]
    else:
        return [(L[0], M[0])] + zap1(L[1:], M[1:])

assert(zap1([1,2],[3,4]) == [(1,3), (2,4)])
assert(zap1([1,2,3,4,5],[6,7,8,9,10]) == [(1,6),(2,7),(3,8),(4,9),(5,10)])

# zap1 is same as zip (stops when one list runs out)
assert(zap1([1,2],[3,4,5]) == [(1,3), (2,4)])
assert(zap1([1,2,3],[4,5]) == [(1,4), (2,5)])

