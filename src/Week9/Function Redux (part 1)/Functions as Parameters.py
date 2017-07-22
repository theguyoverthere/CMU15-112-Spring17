def derivative(f, x):
    h = 10 ** -10
    return (f(x + h) - f(x))/ h

def f(x):
    return 4 * x + 3
print(derivative(f, 2))

def g(x):
    return 4 * x ** 2  + 3

print(derivative(g, 2))