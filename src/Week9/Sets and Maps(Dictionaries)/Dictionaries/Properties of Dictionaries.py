#---------------------------------#
# Dictionaries Map Keys to values #
#---------------------------------#
ages = dict()
key = "fred"
value = 38
ages[key] = value
print(ages[key])
print(ages)
print()

#---------------------------------#
#         Keys are Sets           #
#---------------------------------#
# Keys are unordered
d = dict()
d[2] = 100
d[4] = 200
d[8] = 300
print(d)
print()

# Keys are unique
d = dict()
d[2] = 100
d[2] = 200
d[2] = 300
print(d)
print()

# Keys must be immutable
d = dict()
a = [1]
# d[a] = 42 #TypeError: unhashable type: 'list'

# Values are unrestricted
c = dict()
b = [1, 2]
c["fred"] = b
print(c["fred"])

b += [3]
print(c["fred"])
