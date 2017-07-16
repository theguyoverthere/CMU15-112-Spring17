#------------------------------#
#      Operations on a Set     #
#------------------------------#
# Cardinality of Sets
s = {2, 3, 4, 65, 6}
print(len(s))
print()

# Shallow Copy
s = {1, 2, 3}
t = s.copy()
s.add(4)
print(s)
print(t)
print()

# Remove and return an arbitrary element from s. Raises KeyError if empty
s = {2, 5, 6, 7}
print(s.pop())
print(s)
print()

# Remove all elements from s
s = {1, 2, 3, 4, 5}
s.clear()
print(s, len(s))
print()

#------------------------------------#
# Operations on a set and an element #
#------------------------------------#

# Test for membership in s
s = {1, 2, 3}
print(0 in s) #False
print(1 in s) # True
print()

# Add element x to set s
s = {1, 2, 3}
print(s, 4 in s)
s.add(4)
print(s, 4 in s)
print()

# Remove element x from set s, raises KeyError is not present
s = {1, 2, 3}
print(s, 3 in s)
s.remove(3)
print(s, 3 in s)
print()

# Remove element x from set s if present
s = {1, 2, 3}
print(s, 3 in s)
s.discard(3)
print(s, 3 in s)
s.discard(3) # Does not crash
print(s, 3 in s)
print()

#---------------------------------------------------#
# Operations on two sets (or a set and an iterable) #
#---------------------------------------------------#

# Test whether every element in s is in t
print({1, 2} <= {1}, {1, 2}.issubset({1}))
print({1, 2} <= {1, 2}, {1, 2}.issubset({1, 2}))
print({1, 2} <= {1, 2, 3}, {1, 2}.issubset({1, 2, 3}))
print()

# Test whether every element in t is in s
print({1, 2} >= {1}, {1, 2}.issuperset({1}))
print({1, 2} >= {1, 2}, {1, 2}.issuperset({1, 2}))
print({1, 2} >= {1, 2, 3}, {1, 2}.issuperset({1, 2, 3}))
print()

# New set with elements from both s and t
print({1, 2} | {1}, {1, 2}.union({1}))
print({1, 2} | {1, 3}, {1, 2}.union({1, 3}))
s = {1, 2}
t = s | {1, 3}
print(s, t)
print()

# New set with elements common to both s and t
print({1, 2} & {1}, {1, 2}.intersection({1}))
print({1, 2} & {1, 3}, {1, 2}.intersection({1, 3}))
s = {1, 2}
t = s & {1, 3}
print(s, t)
print()

# New set with elements in s but not in t
print({1, 2} - {1}, {1, 2}.difference({1}))
print({1, 2} - {1, 3}, {1, 2}.difference({1, 3}))
s = {1, 2}
t = s - {1, 3}
print(s, t)
print()

# Symmetric Difference - New set with elements in either s or t but not in both
print({1, 2} ^ {1}, {1, 2}.symmetric_difference({1}))
print({1, 2} ^ {1, 3}, {1, 2}.symmetric_difference({1, 3}))
s = {1, 2}
t = s ^ {1, 3}
print(s, t)
print()

# Modify s adding all elements in t
s = {1, 2}
t = {1, 3}
u = {2, 3}

s.update(u)
t |= u
print(s, t, u)
print()

# Modify s keeping only elements also found in t
s = {1, 2}
t = {1, 3}
u = {2, 3}

s.intersection_update(u)
t &= u
print(s, t, u)

# Modify s removing all elements found in t
s = {1, 2}
t = {1, 3}
u = {2, 3}

s.difference_update(u)
t -= u
print(s, t, u)

# Modify s keeping elements from s or t but not both
s = {1, 2}
t = {1, 3}
u = {2, 3}

s.symmetric_difference_update(u)
t ^= u
print(s, t, u)
