def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper

@memoize
def fib(n):

    if n < 2:
        # Base case: fib(0) = fib(1) are both 1
        return 1
    else:
        # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
        return fib(n - 1, ) + fib(n - 2)

print([fib(n) for n in range(15)])