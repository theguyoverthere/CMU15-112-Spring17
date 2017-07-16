s = set([2, 3, 4])
print(3 in s)
print(4 in s)
print(5 in s)

for x in range(7):
    if x not in s:
        print(x)
