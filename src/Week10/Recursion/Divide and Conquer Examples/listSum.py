def listSum(l):
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return l[0]
    else:
        mid = len(l) // 2
        return listSum(l[:mid]) + listSum(l[mid:])

print(listSum([]))
print(listSum([1]))
print(listSum([1, 2]))
print(listSum([1,2, 3]))