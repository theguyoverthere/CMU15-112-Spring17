def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

assert(gcd(42, 30) == 6)
assert(gcd(2**5 * 3**4 * 5**2, 2**3 * 3**8 * 7) == (2**3 * 3**4))