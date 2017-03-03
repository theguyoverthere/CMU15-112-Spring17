#################################################
# Week2 Practice
#################################################

import cs112_s17_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Tue Lecture
#################################################

def digitCount(n):
    if n == 0: return 1

    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def hasConsecutiveDigits(n):
    if abs(n) < 10: return False

    n = abs(n)
    lastDigit = -1

    while n > 0:
        currentDigit =  n % 10
        if currentDigit == lastDigit: return True
        lastDigit = currentDigit  # Save the last digit
        n //= 10                  # Discard last digit
    return False

def gcd(m, n):
    # Euclid's theorem : gcd(m, n) = gcd(n, m % n)

    while n > 0:
        m, n = n, m % n  # Everything on the right is computed BEFORE the assignment
                         # takes place.
    return m

def isPrime(n):
    if n == 2:
        return True
    elif (n < 2) or (n % 2 == 0):
        return False

    for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
        if n % factor == 0:
            return False
    return True


def pi(n):
    count = 0
    for i in range(2, n + 1):
        if isPrime(i):
            count += 1
    return count

def h(n):
    if n <= 0: return 0
    harmonicSum = 0.0

    for i in range(1, n + 1):
        harmonicSum += (1/i)

    return harmonicSum

def estimatedPi(n):
    if n <= 2: return 0
    return int (roundHalfUp(n / (h(n) - 1.5)))


def estimatedPiError(n):
    if n <= 2 : return 0

    return abs(pi(n) - estimatedPi(n))


def sumOfDigits(n):
    digitSum = 0

    while n > 0:
        digitSum += n % 10
        n //= 10

    return digitSum

def nthAdditivePrime(n):
    found = 0
    guess = 1

    # Keep iterating and each time a Prime is found, make note of it.
    # Once the nth, value is found, return the guess.

    while found <= n:
        guess += 1
        if isPrime(guess) and isPrime(sumOfDigits(guess)):
            found += 1
    return guess

def isPerfectNumber(n):
    if n <= 1 : return False

    divisorSum = 0

    for divisor in range(1, math.floor(n  ** 0.5) + 1):
        if n % divisor == 0:
            divisorSum += divisor
            divisorSum += (n // divisor) # Divisors appear in pairs, but we're only
                                         # picking up the one below the square root.

    # Because we're starting division at 1, we're including the pair divisor i.e.
    # n itself in the divisorSum.
    return divisorSum == 2 * n

def nthPerfectNumber(n):
    found = 0
    guess = 0
    while found  <= n:
        guess += 1
        if isPerfectNumber(guess):
            found += 1
    return guess

#################################################
# Wed Recitation
#################################################

def minDigit(n):
    smallestDigit = n % 10

    while n > 0:
        nthDigit = n % 10
        if nthDigit < smallestDigit:
            smallestDigit = nthDigit
        n //= 10

    return smallestDigit

def numConsecutiveDigits(nthDigit, n):
    numCount = 0

    while n % 10 == nthDigit:
        numCount += 1
        n //= 10
    return numCount

def longestDigitRun(n):
    m = n = abs(n)
    smallestDigit  = -1  # Store the integer
    maxLength      =  0  # Store the associated consecutive length.
    currentLength  =  0  # Consecutive length for the current iteration.

    while n > 0:
        nthDigit = n % 10  # Partition the integer into two parts.
        n //= 10

        currentLength = numConsecutiveDigits(nthDigit, n)

        if currentLength > maxLength:
            maxLength     = currentLength
            smallestDigit = nthDigit
        elif currentLength == maxLength:
            smallestDigit = min(nthDigit, smallestDigit)

    if smallestDigit == -1: return minDigit(m)

    return smallestDigit


def numConsecutiveDecreasingDigits(n):
    digitCount = 1
    numSequence     = 0

    while n > 0:
        nthDigit = n % 10
        mthDigit = (n % 100) // 10

        # We have either reached the leftmost digit or found one which is in
        # an incorrect order.
        if (mthDigit == 0) or (nthDigit <= mthDigit): break

        numSequence += nthDigit * (10 ** (digitCount - 1))
        digitCount += 1

        n //= 10

    numSequence += nthDigit * (10 ** (digitCount - 1))

    return digitCount, numSequence


def longestIncreasingRun(n):

    maxLength       = 0  # Store the associated consecutive length.
    longestSequence = 0  # Longest increasing sequence so far.

    while n > 0:
        currentLength   = 0 # Consecutive length for the current iteration.
        currentSequence = 0 # Value of the current sequence of increasing digits.

        currentLength, currentSequence = numConsecutiveDecreasingDigits(n)

        if currentLength > maxLength:
            maxLength       = currentLength
            longestSequence = currentSequence
            n //= (10 ** (currentLength - 1))

        elif currentLength == maxLength:
            longestSequence = max(currentSequence, longestSequence)

        n //= 10

    return longestSequence

def isPalindrome(n):
    numDigits = digitCount(n)

    while n > 0:
        rDigit = n % 10
        lDigit = n // (10 ** (numDigits - 1))

        if rDigit != lDigit: return False

        #Truncate leftmost digit followed by the rightmost digit
        n -= (lDigit * (10 ** (numDigits - 1)))
        n //= 10
        numDigits-= 2

    return True

def nthPalindromicPrime(n):
    found = -1
    guess = 1
    while found  < n:
        guess += 1
        if isPrime(guess) and isPalindrome(guess):
            found += 1
    return guess

def nthLeftTruncatablePrime(n):
    found =  0
    guess =  1

    # Keep iterating and each time a Prime is found, make note of it.
    # Once the nth, value is found, return the guess.

    while found <= n:
        guess += 1
        numDigits = digitCount(guess)

        if isPrime(guess):
            g = guess

            while g > 0:
                lDigit = g // (10 ** (numDigits - 1))
                g -= (lDigit * (10 ** (numDigits - 1)))
                numDigits -= 1

                if (g > 0) and (not isPrime(g)): break

            if g == 0 : found += 1
    return guess

def nthCarolPrime(n):
    found =  0
    k     =  0

    # Keep iterating and each time a Carol Prime is found,
    # make note of it. Once the nth, value is found, return
    # the Carol Number.

    while found <= n:
        k += 1
        nextCarolNum = (((2 ** k) - 1) ** 2) - 2

        if isPrime(nextCarolNum):
            found += 1

    return nextCarolNum

#################################################
# Thu Lecture
#################################################

def sumOfSquaresOfDigits(n):
    sumSquare = 0

    while n > 0:
        nthDigit = n % 10
        sumSquare += (nthDigit ** 2)

        n //= 10

    return sumSquare

def isHappyNumber(n):

    if   n <= 0: return False
    if   n == 1: return True
    elif n == 4: return False # Special Case

    while True:
        if (n == 1) or (n == 4): break
        n = sumOfSquaresOfDigits(n)
    return n == 1

def nthHappyNumber(n):
    guess = 0
    found = -1
    while found < n:
        guess += 1
        if isHappyNumber(guess):
            found += 1

    return guess

def isHappyPrime(n):
    return isPrime(n) and isHappyNumber(n)

def nthHappyPrime(n):
    found = -1
    guess = 1
    while found  < n:
        guess += 1
        if isHappyPrime(guess):
            found += 1
    return guess

def countDigitOccurrence(n, digit):
    digitCount = 0

    while n > 0:
        nthDigit = n % 10

        if nthDigit == digit:
            digitCount += 1

        n //= 10

    return digitCount

def mostFrequentDigit(n):
    if n == 0: return 0 # Special Case.

    n = abs(n)
    m = n

    maxCount      = 0
    maxCountDigit = -1
    currentCount  = 0
    while n > 0:
        nthDigit = n % 10
        currentCount = countDigitOccurrence(m, nthDigit)

        if currentCount > maxCount:
            maxCount = currentCount
            maxCountDigit = nthDigit
        elif currentCount == maxCount:
            maxCountDigit = min(nthDigit, maxCountDigit)

        n //= 10
    return maxCountDigit

def isPowerfulNumber(n):
    if n == 1: return True

    isInvalid = False

    for divisor in range(2, n + 1):
        if n % divisor == 0 and isPrime(divisor):
            if n % (divisor ** 2) != 0 :
                isInvalid = True

    return not isInvalid

def nthPowerfulNumber(n):
    found = 0
    guess = 0

    while found  <= n:
        guess += 1
        if isPowerfulNumber(guess):
            found += 1
    return guess

def rotateNumber(n, numDigits):
    nthDigit = n % 10
    n //= 10
    n += nthDigit * (10 ** (numDigits -1))

    return n

def isCircularPrime(n):
    numDigits = digitCount(n)

    if isPrime(n):
        for i in range(numDigits):
            n = rotateNumber(n, numDigits)
            if not isPrime(n):
                return False
        return True
    return False

def nthCircularPrime(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isCircularPrime(guess):
            found += 1
    return guess

def findZeroWithBisection(f, x0, x1, epsilon):
    while not almostEqual(x0, x1, epsilon):
        xmid = (x0 + x1) / 2

        if f(xmid) == 0:
            return xmid
        elif f(x0) * f(x1) >= 0:
            return None
        elif f(xmid) * f(x0) > 0:
            x0 = xmid
        else:
            x1 = xmid
    return (x0 + x1) / 2

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Test digitCount()...', end='')
    assert(digitCount(0) == 1)
    assert(digitCount(5) == 1)
    assert(digitCount(-5) == 1)
    assert(digitCount(42) == 2)
    assert(digitCount(-42) == 2)
    assert(digitCount(121) == 3)
    assert(digitCount(-121) == 3)
    assert(digitCount(-10002000) == 8)
    print('Passed')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()... ', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(330) == True)
    assert(hasConsecutiveDigits(3003) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed.')

def testGcd():
    print('Testing gcd()... ', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed.')

def testPi():
    print('Testing pi()... ', end='')
    assert(pi(1) == 0)
    assert(pi(2) == 1)
    assert(pi(3) == 2)
    assert(pi(4) == 2)
    assert(pi(5) == 3)
    assert(pi(100) == 25)  # there are 25 primes in the range [2,100]
    print('Passed.')

def testH():
    print('Testing h()... ', end='')
    assert(almostEqual(h(0),0))
    assert(almostEqual(h(1),1/1            ))  # h(1) = 1/1
    assert(almostEqual(h(2),1/1 + 1/2      ))  # h(2) = 1/1 + 1/2
    assert(almostEqual(h(3),1/1 + 1/2 + 1/3))  # h(3) = 1/1 + 1/2 + 1/3
    print('Passed.')

def testEstimatedPi():
    print('Testing estimatedPi()... ', end='')
    assert(estimatedPi(100) == 27)
    print('Passed.')

def testEstimatedPiError():
    print('Testing estimatedPi()... ', end='')
    assert(estimatedPiError(100) == 2) # pi(100) = 25, estimatedPi(100) = 27
    assert(estimatedPiError(200) == 0) # pi(200) = 46, estimatedPi(200) = 46
    assert(estimatedPiError(300) == 1) # pi(300) = 62, estimatedPi(300) = 63
    assert(estimatedPiError(400) == 1) # pi(400) = 78, estimatedPi(400) = 79
    assert(estimatedPiError(500) == 1) # pi(500) = 95, estimatedPi(500) = 94
    print('Passed.')

def testNthPrime():
    print('Testing nthPrime()... ', end='')
    assert(nthPrime(0) == 2)
    assert(nthPrime(1) == 3)
    assert(nthPrime(2) == 5)
    assert(nthPrime(3) == 7)
    assert(nthPrime(10) == 31)
    assert(nthPrime(20) == 73)
    assert(nthPrime(30) == 127)
    print('Passed.')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed.')

def testNthPerfectNumber():
    print('Testing nthPerfectNumber()... ', end='')
    assert(nthPerfectNumber(0) == 6)
    assert(nthPerfectNumber(1) == 28)
    assert(nthPerfectNumber(2) == 496)  
    assert(nthPerfectNumber(3) == 8128) # this can be slow 
    print('Passed.')

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    print('Passed.')

def testLongestIncreasingRun():
    print('Testing longestIncreasingRun()... ', end='')
    assert(longestIncreasingRun(27648923679) == 23679)
    assert(longestIncreasingRun(123345) == 345)
    assert(longestIncreasingRun(1232) == 123)
    assert(longestIncreasingRun(0) == 0)
    assert(longestIncreasingRun(1) == 1)
    assert(longestIncreasingRun(10012301230123) == 123)
    assert(longestIncreasingRun(12345678987654321) == 123456789)
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()... ', end='')
    assert(nthPalindromicPrime(0) == 2)
    assert(nthPalindromicPrime(1) == 3)
    assert(nthPalindromicPrime(5) == 101)
    assert(nthPalindromicPrime(10) == 313)
    print('Passed.')

def testNthLeftTruncatablePrime():
    print('Testing nthLeftTruncatablePrime()... ', end='')
    assert(nthLeftTruncatablePrime(0) == 2)
    assert(nthLeftTruncatablePrime(10) == 53)
    assert(nthLeftTruncatablePrime(1) == 3)
    assert(nthLeftTruncatablePrime(5) == 17)
    print('Passed.')

def testNthCarolPrime():
    print('Testing nthCarolPrime()... ', end='')
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(6) == 16769023)
    print('Passed.')

def testSumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
    assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
    assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4+9+16 = 29
    print("Passed.")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed.")

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    print("Passed.")

def testIsHappyPrime():
    print("Testing isHappyPrime()...", end="")
    assert(isHappyPrime(1) == False)
    assert(isHappyPrime(2) == False)
    assert(isHappyPrime(3) == False)
    assert(isHappyPrime(7) == True)
    assert(isHappyPrime(10) == False)
    assert(isHappyNumber(13) == True)
    print("Passed.")

def testNthHappyPrime():
    print("Testing nthHappyPrime...", end="")
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(10) == 167)
    assert(nthHappyPrime(20) == 397)
    print("Passed.")

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()... ', end='')
    assert(mostFrequentDigit(0) == 0)
    assert(mostFrequentDigit(1223) == 2)
    assert(mostFrequentDigit(12233) == 2)
    assert(mostFrequentDigit(-112233) == 1)
    assert(mostFrequentDigit(1223322332) == 2)
    assert(mostFrequentDigit(123456789) == 1)
    assert(mostFrequentDigit(1234567789) == 7)
    assert(mostFrequentDigit(1000123456789) == 0)
    print('Passed.')

def testNthPowerfulNumber():
    print('Testing nthPowerfulNumber()... ', end='')
    assert(nthPowerfulNumber(0) == 1)
    assert(nthPowerfulNumber(1) == 4)
    assert(nthPowerfulNumber(2) == 8)
    assert(nthPowerfulNumber(3) == 9)
    assert(nthPowerfulNumber(4) == 16)
    assert(nthPowerfulNumber(5) == 25)
    assert(nthPowerfulNumber(10) == 64)
    assert(nthPowerfulNumber(15) == 121)
    assert(nthPowerfulNumber(20) == 196)
    print('Passed.')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(1) == 3)
    assert(nthCircularPrime(2) == 5)
    assert(nthCircularPrime(10) == 73)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(16) == 199)
    print('Passed.')

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testDigitCount()
    testHasConsecutiveDigits() 
    testGcd()
    testPi()
    testH()
    testEstimatedPi()
    testEstimatedPiError()
    testNthAdditivePrime()
    testNthPerfectNumber() 
    testLongestDigitRun()
    testLongestIncreasingRun()
    testNthPalindromicPrime()
    testNthLeftTruncatablePrime()
    testNthCarolPrime()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyNumber()
    testNthHappyPrime()
    testMostFrequentDigit()
    testNthPowerfulNumber()
    testNthCircularPrime()
    testFindZeroWithBisection()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,repr,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
