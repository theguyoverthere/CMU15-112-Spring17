# Try and FAIL, to create a variable-sized 2d List

rows = 3
cols = 2
a = [ [0] * cols] * rows # Error: creates shallow copy

print("This SEEMS Ok. At first.")
print(" a =", a)

a[0][0] = 42
print("But see what happens after a[0][0]= 42")
print(" a =", a)


# https://goo.gl/Mb2UmL
# Visualize what is going on under the hood.
# List multiplication essentially creates a list of pointers to a list!
row = 3
columns = 2

matrix_surprise = [[0] * columns] * rows
matrix = [[0]*columns for i in range(rows)]

