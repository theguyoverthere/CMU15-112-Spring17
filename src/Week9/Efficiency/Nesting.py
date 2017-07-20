# what is the total cost here?
L = [ 52, 83, 78, 9, 12, 4 ]   # assume L is an arbitrary list of length N
for c in L:                    # This loop's body is executed O(N) times
    L[0] += c                  # This is O(1)
    L.sort()                   # This is O(NlogN)
print(L)                       # This is O(N) (why?)
