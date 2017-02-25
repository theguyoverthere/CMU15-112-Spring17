# Local Variable Scope


def f(x):
    print("In f, x =", x)
    x += 5
    return x


def g(x):
    return f(x*2) + f(x*3)


print(g(2))
print("---------------")

# Some More examples


def f(x):
    print("In f, x =", x)
    x += 7
    return round(x / 3)


def g(x):
    x *= 10
    return 2 * f(x)


def h(x):
    x += 3
    return f(x+4) + g(x)


print(h(f(1)))
print("---------------")

# Global Variable Scope

g = 100


def f(x):
    return x + g

print(f(5))
print(f(6))
print(g)
print("---------------")


g = 100

def f(x):
    global g
    g += 1
    return x + g

print(f(5))
print(f(6))
print(g)


