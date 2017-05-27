rows = 3
cols = 2

a = [([0] * cols) for row in range(rows)]
print("This IS ok. At first")
print( " a = ", a)

a[0][0] = 42
print("And see what happens after a[0][0] = 42")
print( " a = ", a)
