import math

def isPrime(n):
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


def nthPrime(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if isPrime(guess):
            found += 1

    return guess

# and let's see a list of the primes
for n in range(10):
    print(n, nthPrime(n))
print("Done!")