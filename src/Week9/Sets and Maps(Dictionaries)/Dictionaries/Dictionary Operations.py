#-------------------------------------#
#      Operations on a Dictionary     #
#-------------------------------------#
# The number of items(key-value pairs) in a dictionary
d = {1:[1, 2, 3, 4, 5, 6], 2:"abc"}
print(len(d))
print()

# New dictionary with a shallow copy of d
d1 = {1: "a"}
d2 = d1.copy()
d1[2] = "b"
print(d1)
print(d2)
print()

# Remove and return an arbitrary(key, value) pair from d, raises KeyError if
# empty
d = {1:"a", 2:"b"}
print(d.popitem())
print(d)
print()

# Remove all items from dictionary
d = {1:"a", 2:"b"}
d.clear()
print(d)
print()

# Iterate over all items in d
d = {1:"a", 2:"b"}
for key in d:
    print(key, d[key])
print()

#----------------------------------------------------#
#  Operations on a Dictionary and a key[and value]   #
#----------------------------------------------------#

# Test if d has the given key
d = {1:"a", 2:"b"}
print(0 in d)
print(1 in d)
print("a" in d)
print()

# Test if d does not have the given key
d = {1:"a", 2:"b"}
print(0 not in d)
print(1 not in d)
print("a" not in d)
print()

# The item of d with the given key. Raises a KeyError if key is not in map
d = {1:"a", 2:"b"}
print(d[1])
#print(d[3]) #KeyError: 3
print()

# Set d[key] to value
d = {1:"a", 2:"b"}
print(d[1])
d[1] = 42
print(d[1])

# The value of the key if key is in dictionary, else default value
d = {1:"a", 2:"b"}
print(d.get(1))     # Works like d[1] here
print(d.get(1, 42)) # Default is ignored
print(d.get(0))     # Doesn't crash
print(d.get(0, 42)) # Default is used

# Remove d[key] from d. Raises KeyError if key is not in d
d = {1:"a", 2:"b"}
print(1 in d)
del d[1]
print(1 in d)
#del d[1] #crash!

#-----------------------------------------------------------#
# Operations on two dictionaries(or a dict and an iterable) #
#-----------------------------------------------------------#
d1 = {1:"a", 2:"b"}
d2 = {2:"c", 3:"d"}
d1.update(d2)
d2[4] = "e"
print(d1)
print(d2)
