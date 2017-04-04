import copy

# Create a list
a = [2, 3, 4]

# Try to copy it
b = a #Error! Not a copy, but an alias
c = copy.copy(a)

# At first, things seem ok
print("At first..")
print("   a =", a)
print("   b =", b)
print("   c =", c)

# Now modify a[0]
a[0] = 42
b[1] = 111
print("But after a[0] = 42")
print("   a =", a)
print("   b =", b)
print("   c =", c)
print("----------------")

#Other ways to copy
a = [2, 3]
b = copy.copy(a)
c = a[:]
d = a + []
e = list(a)
f = copy.deepcopy(a)
g = sorted(a)

a[0] = 42
print(a, b, c, d, e, f, g)