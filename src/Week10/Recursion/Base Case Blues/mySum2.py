def mySum2(L):
    # duplicating built-in sum function recursively, but with a problem...
    # if L == [ ]: return 0
    if len(L) == 0: return 0
    else: return L[0] + mySum2(L[1:])

print(mySum2([0,1,2,3])) # 6 (this works)
print(mySum2(range(4)))  # crash!  IndexError: range object index out of range
