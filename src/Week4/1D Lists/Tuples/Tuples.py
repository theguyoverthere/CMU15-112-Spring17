# Tuple Syntax
t = (1, 2, 3)
print(type(t), len(t), t)

a = [1, 2, 3]
t = tuple(a)
print(type(t), len(t), t)
print("--------------------")

# Tuples are immutable
t = (1, 2, 3)
print(a[0])

# t[0] = 42
print(t[0])
print("--------------------")

# Parallel Tuple Assignment
(x, y) = (1, 2)
print(x)
print(y)

(x, y) = (y, x)
print(x)
print(y)
print("--------------------")

t= (42)
print(type(t), t * 5)

t = (42, )
print(type(t), t * 5)
