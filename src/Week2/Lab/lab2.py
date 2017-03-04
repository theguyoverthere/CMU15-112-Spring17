#################################################
# Lab2
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

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def rotateNumber(n, numDigits):
    nthDigit = n % 10
    n //= 10
    n += nthDigit * (10 ** (numDigits -1))

    return n

def isRotation(x, y):
    numDigits = digitCount(y)

    for i in range(numDigits):
        if x == y: return True
        y = rotateNumber(y, numDigits)

    return False

def isPrime(n):
    if n == 2:
        return True
    elif (n < 2) or (n % 2 == 0):
        return False

    for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
        if n % factor == 0:
            return False
    return True


# Original: 8712, 9801, 87912, 98901, 879912
# Reversed: 2178, 1089, 21978, 10989, 219978
def reverseNumber(n):
    exponent = numDigits = digitCount(n)
    reversedNum = 0

    for i in range(numDigits):
        nthDigit = n % 10
        n //= 10
        reversedNum += nthDigit * (10 ** (exponent - 1))
        exponent -= 1


    return reversedNum

def isEmirpsPrime(n):
    return isPrime(n) and (reverseNumber(n) != n) and isPrime(reverseNumber(n))

def nthEmirpsPrime(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if isEmirpsPrime(guess):
            found += 1
    return guess

def carrylessAdd(x, y):
    nxDigits = digitCount(x)
    nyDigits = digitCount(y)
    carrylessSum = 0

    for i in range(max(nxDigits, nyDigits)):
        nthDigitX = x % 10
        nthDigitY = y % 10

        nthDigitS = nthDigitX + nthDigitY
        if nthDigitS >= 10: nthDigitS -= 10

        carrylessSum += nthDigitS * (10 ** i)
        x //= 10
        y //= 10

    return carrylessSum


def hasEveryDigit(n):
    digit0Present = False
    digit1Present = False
    digit2Present = False
    digit3Present = False
    digit4Present = False
    digit5Present = False
    digit6Present = False
    digit7Present = False
    digit8Present = False
    digit9Present = False

    while n > 0:
        nthDigit = n % 10
        if   nthDigit == 0: digit0Present = True
        elif nthDigit == 1: digit1Present = True
        elif nthDigit == 2: digit2Present = True
        elif nthDigit == 3: digit3Present = True
        elif nthDigit == 4: digit4Present = True
        elif nthDigit == 5: digit5Present = True
        elif nthDigit == 6: digit6Present = True
        elif nthDigit == 7: digit7Present = True
        elif nthDigit == 8: digit8Present = True
        elif nthDigit == 9: digit9Present = True

        n //= 10

    return digit0Present and digit1Present and \
           digit2Present and digit2Present and \
           digit3Present and digit4Present and \
           digit5Present and digit6Present and \
           digit7Present and digit8Present and \
           digit9Present

def hasProperty309(n):
    return hasEveryDigit(n ** 5)

def nthWithProperty309(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if hasProperty309(guess):
            found += 1

    return guess

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed.')

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()... ', end='')
    assert(nthEmirpsPrime(0) == 13)
    assert(nthEmirpsPrime(5) == 73)
    assert(nthEmirpsPrime(10) == 149)
    assert(nthEmirpsPrime(20) == 701)
    assert(nthEmirpsPrime(30) == 941)
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(5) == 635)
    assert(nthWithProperty309(6) == 662)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testIsRotation()
    testNthEmirpsPrime()
    testCarrylessAdd()
    testNthWithProperty309()

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
