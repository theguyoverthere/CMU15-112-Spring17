a = [2, 3, 5, 7]

# Method 1
print("Here are the items in a:")
for item in a:
    print(item)

# Method 2
print("Here are the items in a with their indices")
for index in range(len(a)):
    print("a[" + str(index) + "]=", a[index])

#Looping Backwards
print("And here are the items in reverse:")
for index in range(len(a)):
    revIndex = len(a) - 1 - index
    print("a[" + str(revIndex) + "]=", a[revIndex])

#Looping backward with reversed list
print("And here are the items in reverse")
for item in reversed(a):
    print(item)

#Looping backward with reversed list - Destructive
a.reverse()
print("And here are the items in reverse")
for item in a:
    print(item)


