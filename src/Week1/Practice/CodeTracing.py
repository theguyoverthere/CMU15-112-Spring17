import math
import decimal


def p(x): print(x, end='   ')  # prints and stays on same line

p(3 - 1 + 2 * 6 // 5)
p(3 - 1 + 2 * 6 / 5)
p(2**4/10 + 2**4//10)
p(max(8/3,math.ceil(8/3)))

print()

# Note: we provide roundHalfUp and roundHalfEven for you.
# Use these instead of the builtin round function, since that
# function may not behave as you expect.

# A 1.5 can be rounded up or rounded down to 1 or 2. Since we have a tie, the result will
# depend on the function being used to round.
# RoundHalfAwayFromZero(x) Rounds to nearest, ties going away from zero. 1.5 → 2, -1.5 → -2.
# RoundHalfEven(x)         Rounds to nearest, ties going to nearest even integer. 1.5 → 2, 2.5 → 2.


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def roundHalfEven(d):
    # Round to nearest with ties going to nearest even integer.
    rounding = decimal.ROUND_HALF_EVEN
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def p(x): print(x, end='   ')  # prints and stays on same line
p(round(1.5))                  # 2 By default - Round Half even in Python 3
p(roundHalfUp(1.5))            # 2 - Rounding goes away from 0
p(roundHalfEven(1.5))          # 2 - Rounding towards the nearest EVEN integer

print()

p(round(2.5))                  # 2 By default - Round Hald even in Python 3
p(roundHalfUp(2.5))            # 3 Round away from 3
p(roundHalfEven(2.5))          # 2 Round towards nearest integer

print()


def p(x): print(x, end='   ')  # prints and stays on same line


def f(x, y):
    if x > y:
        if x > 2*y : p('A')
        else : p('B')
    else:
        p('C')


def g(x, y):
    if abs(x % 10 - y % 10) < 2 : p('D')
    elif x % 10 > y % 10 : p('E')
    else:
        if x//10 == y//10 : p('F')
        else : p('G')

f(4, 2)      # B
f(2, 3)      # C
f(5, 2)      # A

print()
g(11, 14)    # F
g(11, 24)    # G
g(207, 6)    # D
g(207, 5)    # E

print()


def f(x): return 4*x + 2


def g(x): return f(x//2 + 1)


def h(x):
    print(f(x-3))    # x = 6, f(3) = (4 * 3 + 2) = 14
    x -= 1           # x = 5
    print(g(x) + x)  # g(5) + 5 = f(5//2 + 1) + 5 = f(3) + 5 = (4 * 3 + 2) + 5 = 19
    x %= 4           # x = 1

    return g(f(x) % 4) // 2
    # g(f(1) % 4) // 2
    # = g((4 * 1 + 2) % 4) // 2
    # = g(2) //2 = f(2//2 + 1) //2
    # = f(2) //2  = (4 * 2 + 2) //2
    # = 10   // 2

print(1 + h(6))      # 1 + 5 = 6


def rc1(n):
    if (n < 0) or (n > 99): return False
    d1 = n % 10
    d2 = n // 10
    m = 10 * d1 + d2
    # => n = 0 to 11
    # => m = 1 to 10
    # => m = 10 * d1 + d2 = 1 to 10
    # d1 = 0 => n = 10
    # d2 = 1
    # => n = 10, m = 1
    return (m < n) and (n < 12)

print(rc1(10))


def rc2(n):
    if (n <= 0) or (n > 99): return False
    # => n = 1 to 99
    if n // 2 * 2 != n: return False
    # => n // 2 = n / 2
    # => n must be even                     ... (1)
    # => n = 2, 4....98
    if n // 5 * 5 != n: return False
    # => n // 5 = n / 5
    # => n is multiple of 5                 ... (2)
    # From (1) and (2), n must be a multiple of both 2 and 5
    return n // 7 * 7 == n
    # => n // 7 = n /7
    # => n is a multiple of 7               ... (3)
    # From (1), (2) and (3), n must be 70

print(rc2(70))
