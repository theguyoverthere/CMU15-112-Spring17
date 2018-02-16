# MIT 6.0001
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        result =  fib_efficient(n - 1, d) + fib_efficient(n -2 , d)
        d[n] = result
        return result

d = {1:1, 2:1}
print(fib_efficient(34, d))