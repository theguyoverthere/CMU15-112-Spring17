import math
import decimal

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def fasterIsPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True # Special Case
    elif n % 2 == 0:
        return False
    else:
        for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
            if n % factor == 0:
                return False
        return True

# And take it for a spin
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")
print()



