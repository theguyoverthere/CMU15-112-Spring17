def ct4(L):
    result = [ ]
    M = L[:] # same as M = copy.copy(L)
    if (M == L): result.append(1)
    if (M is L): result.append(2)
    if (M[0] == L[0]): result.append(3)
    if (M[0] is L[0]): result.append(4)
    return result

print(ct4([5,7,6]))
