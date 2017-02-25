def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    else:
        print("D", end="")
        if (x == 1):
            print("E", end="")
        else:
            print("F", end="")
    print("G")

f(0)
f(1)
f(2)


def abs5(n):
    if (n >= 0):
        return n
    else:
        return -n

# or, if you prefer...

def abs6(n):
    if (n >= 0):
        sign = +1
    else:
        sign = -1
    return sign * n

print("abs5(5) =", abs5(5), "and abs5(-5) =", abs5(-5))
print("abs6(5) =", abs6(5), "and abs6(-5) =", abs6(-5))
