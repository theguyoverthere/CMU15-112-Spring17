def listSum(L):
    if len(L) == 0:
        return 0
    else:
        mid = len(L) // 2
        return listSum(L[:mid]) + listSum(L[mid:])

print(listSum([2])) # 28