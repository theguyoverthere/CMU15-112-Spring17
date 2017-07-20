# what is the total cost here?
L = [ 52, 83, 78, 9, 12, 4 ]   # assume L is an arbitrary list of length N
L.sort()                       # This is O(NlogN)
L.sort(reverse=True)           # This is O(NlogN)
L[0] -= 5                      # This is O(1)
print(L.count(L[0]) + sum(L))  # This is O(N) + O(N)
