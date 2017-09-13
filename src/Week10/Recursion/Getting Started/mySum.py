def mySum(L):
    # Duplicating the built in "sum" function.
    if not L: return 0
    else: return L[0] + mySum(L[1:])

print(mySum([0,1,2,3])) # 6 (this works)
print(mySum(range(4)))  # crash!  IndexError: range object index out of range
