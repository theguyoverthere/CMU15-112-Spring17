# Visualize on pythontutor.com

def ct2(a, b):
    a += [3]
    a = a + [4]

    a = [4, 3, 4]
    for c in a:
        for i in range(len(b)):
            if (b[i] not in a):
                print("A", end="")
                b[i] += c
            elif (c % 2 == 1):
                print("B", end="")
                b += [c]
            elif (b[-1] != c):
                print("C", end="")
                b = b + [c]
    return (a,b)
a = [4]
b = [2,3]
print(ct2(a,b))
print(a,b)