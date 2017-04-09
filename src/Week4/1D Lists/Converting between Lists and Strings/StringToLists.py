# use list(s) to convert a string to a list of characters
a = list("wahooo")
print(a)

# use s1.split(s2) to convert a string to a list of strings delimited by s2
a = "How are you doing today?".split(" ")
print(a)

# use "".join(a) to convert a list of characters to a single string
s = "-".join(a)
print(s)

# "".join(a) also works on a list of strings (not just single characters)
a = ["parsley", " ", "is", " ", "gharsley"] # by Ogden Nash!
s = "".join(a)
print(s)  # prints: parsley is gharsley

s = "How are you doing today?"
a = s.split()
print(a)

s = "How-are-you-doing-today?"
a = s.split("-")
print("-".join(s.split("-")))







