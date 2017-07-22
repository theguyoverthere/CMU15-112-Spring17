def derivative(f, x):
    h = 10 ** -10
    return (f(x + h) - f(x))/ h

print(derivative(lambda x: (3 * (x ** 5)) + 2, 2)) # about 240, 15*x**4 at x==2

myF = lambda x: 10 * x + 42

print(myF(5)) # 92
print(derivative(myF, 5)) # about 10
