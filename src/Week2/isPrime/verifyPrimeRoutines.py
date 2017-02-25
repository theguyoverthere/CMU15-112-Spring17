import math

def isPrime(n):
    if n < 2:
        return False
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True

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


# Verify these are the same
for n in range(100):
    assert(isPrime(n) == fasterIsPrime(n))
print("They seem to work the same!")

# Now let's see if we really sped things up
import time
bigPrime = 102030407 # Try 499, 1010809, or 10101023, or 102030407
print("Timing isPrime(", bigPrime, ")", end=" ")

time0 = time.time()
print(", returns ", isPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1 - time0) * 1000, "ms")

print("Timing fasterIsPrime(", bigPrime, ")", end=" ")

time0 = time.time()
print(", returns ", fasterIsPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1 - time0) * 1000, "ms")
