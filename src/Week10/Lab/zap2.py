def zap2(L, M, depth=0):
    # If both the lists get reduced to the same length,
    # at the same time, it means that they are equal in length.
    if len(L) == 1 and len(M) == 1:
        return [(L[0], M[0])]

    # If we've run of elements in L, create a dummy list with None values
    # of a length equal to the current length of M and recurse!
    if len(L) == 0:
        return zap2([None] * len(M), M)

    # If we've run of elements in M, create a dummy list with None values
    # of a length equal to the current length of L and recurse!
    elif len(M) == 0:
        return zap2(L, [None] * len(L))
    else:
        return [(L[0], M[0])] + zap2(L[1:], M[1:])


assert(zap2([1,2],[3,4]) == [(1,3), (2,4)])
# zap2 uses None when no values are available
assert(zap2([1, 2],[3, 4, 5, 6]) == [(1,3), (2,4), (None, 5), (None, 6)])
assert(zap2([1,2,3, 4],[4,5]) == [(1,4), (2,5), (3, None), (4, None)])
