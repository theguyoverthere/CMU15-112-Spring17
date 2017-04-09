# Sieve of Eratosthenes

# This function returns a list of prime numbers
# up to n (inclusive), using the Sieve of Eratosthenes.
# See http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieve(n):
    isPrime = [True] * (n + 1)
    primes = []
    isPrime[0] = isPrime[1] = False

    for prime in range(n + 1):
        if isPrime[prime] == True:
            primes.append(prime)

            for multiple in range(2 * prime, n + 1, prime):
                isPrime[multiple] = False

    return primes

print(sieve(100000))