def f(n):
    if n == 42:
        raise Exception("I take exception to 42")
    return n + 1

try:
    print(f(5))
    print(f(42))
    print(f(50))
except Exception as error:
    print("Caught exception:", error)

