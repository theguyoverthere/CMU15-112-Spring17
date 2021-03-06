import math
import decimal

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



