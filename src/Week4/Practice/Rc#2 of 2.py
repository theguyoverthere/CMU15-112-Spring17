# Unsolved.
def rc2(L):
  assert((isinstance(L, list)) and (None not in L))
  i = 0
  while (L[i] !=  None):
    j = L[i]
    L[i]  = None
    i = j
    a = [None]*2
  return  (L  == a + [-1] + a)


L = [-1, -1, 1]
print(rc2(L))