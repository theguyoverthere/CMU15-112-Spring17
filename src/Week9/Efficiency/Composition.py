# what is the total cost here?
def f(L):             # assume L is an arbitrary list of length N
    L1 = sorted(L)    # This is O(NlogN)
    return L1         # This is O(1)

def g(L):             # assume L is an arbitrary list of length N
    L1 = L * len(L)   # This is O(N**2) (why?)
    return L1         # This is O(1)

L = [ 52, 83, 78, 9, 12, 4 ]   # assume L is an arbitrary list of length N
L = f(g(L))                    # What is the big-oh of this?
print(L)                       # This is O(N**2) (why?)
