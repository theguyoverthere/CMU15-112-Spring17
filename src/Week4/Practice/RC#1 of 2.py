def rc1(M):
  assert(isinstance(M,  list) and (len(M) ==  5))
  for i in range(-1, 3):
    assert(M[i] == M[i-1] + i)
  return  (sum(M) ==  15)

print(rc1([2, 3, 5, 3, 2]))