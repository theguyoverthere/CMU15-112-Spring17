def listSum(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + listSum(L[1:])

print(listSum([2,3,5,7,11])) # 28