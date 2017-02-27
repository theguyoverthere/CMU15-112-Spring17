#
# Lets first assume that ties are not possible. Solve the simpler case.
#

def numConsecutiveDigits(nthDigit, n):
    numCount = 0

    while n % 10 == nthDigit:
        numCount += 1
        n //= 10
    return numCount

def longestDigitRun(n):
    n = abs(n)

    prevMax          = -1  # Store the integer
    prevMaxLength    =  0  # Store the associated consecutive length.
    currentLength    =  0  # Consecutive length for the current iteration.

    while n > 0:
        nthDigit = n % 10  # Partition the integer into two parts.
        n //= (10 ** (currentLength + 1 ))
        currentLength = numConsecutiveDigits(nthDigit, n)

        if currentLength > prevMaxLength:
            prevMaxLength = currentLength
            prevMax       = nthDigit

    return prevMax

print(longestDigitRun(32220))
