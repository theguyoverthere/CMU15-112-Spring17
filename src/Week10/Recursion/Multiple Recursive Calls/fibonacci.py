# Note: as written, this function is very inefficient!
# We need to use "memoization" to speed it up! See below for details!)
def fib(n, depth = 0):

    if n < 2:
        # Base case: fib(0) = fib(1) are both 1
        return 1
    else:
        # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
        return fib(n - 1, depth + 1) + fib(n - 2, depth + 1)

print([fib(n) for n in range(15)])