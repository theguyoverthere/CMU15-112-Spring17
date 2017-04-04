#Create some lists
a = [2, 3, 5, 3, 7, 10000]
b = [2, 3, 5, 3, 7]
c = [2, 3, 5, 3, 8]
d = [2, 3, 5]

print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)

print("---------------")
print("a == b", a == b)
print("a == c", a == c)
print("a != b", a != b)
print("a != c", a != c)

print("---------------")

# The comparison takes place at the first element where the two lists
# differ.
print("a < c ", a < c)

# The first three elements in a and d are the same, however a has more
# number of elements.
print("a < d ", a < d)