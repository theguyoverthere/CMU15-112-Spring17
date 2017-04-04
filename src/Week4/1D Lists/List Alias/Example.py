# Create a list
a = [ 2, 3, 5, 7 ]

# Create an alias to the list
b = a

# We now have two references (aliases) to the SAME list
a[0] = 42
b[1] = 99
print(a)
print(b)
