def leftmostDigit(n):

    n = abs(n)
    while n >= 10:
        n //= 10 
    return n

print(leftmostDigit(72658489290098))