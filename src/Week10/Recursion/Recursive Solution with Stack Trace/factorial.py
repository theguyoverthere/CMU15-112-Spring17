def factorial(n, depth=0):
    print(" " * depth + "factorial(" + str(n) + ")")

    if n == 1:
        result = 1
    else:
        result = n * factorial(n - 1, depth + 1)

    print(" " * depth + "..." + str(result))
    return result

print(factorial(5))
