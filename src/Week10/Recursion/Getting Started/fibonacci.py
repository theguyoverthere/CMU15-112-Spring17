def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(3):
    print(fibonacci(n))

assert([fibonacci(n) for n in range(10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
