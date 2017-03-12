# 1. Indexing a single character
# ------------------------------
s  = "abcdefgh"
print(s)

print(s[0])
print(s[1])
print(s[2])
print(s[len(s) - 1])
# print(s[len(s)]) # Crashes - index out of range
print("----------")

# 2. Negative Indices
# -------------------
s  = "abcdefgh"
print(s)
print(s[-1])
print(s[-2])
print("----------")

# 3. Slicing a range of characters
# --------------------------------
s  = "abcdefgh"
print(s)
print(s[0:3])
print(s[1:3])
print(s[2:3])
print(s[3:3])
print("----------")

# 3. Slicing with default parameters
# ----------------------------------
s  = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print()
print(s[:] == s[0:len(s)])
print("----------")

# 4. Slicing with a step parameter
# ----------------------------------
print("This is not common, but perfectly ok")
s  = "abcdefgh"
print(s)
print(s[1:7:2])
print(s[1:7:3])
print("----------")

# 5. Reversing a string
#----------------------
s  = "abcdefgh"
print(s)

print("This works but is confusing")
print(s[::-1])
print()

print("This works and is not so confusing")
print(s[0:len(s):-1])
print()

print("This also works but is still confusing")
print("".join(reversed(s)))
print()


print("Best way: write your own reverseString() function")
def reverseString(s):
    return s[::-1]

print(reverseString(s))
print("----------")