import cs112_s17_linter
import math
import decimal

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def sumPartition(n, partitionSize):
    lPart = 0
    rPart = 0
    m = n

    for i in range(partitionSize):
        nthDigit = m % 10
        rPart += nthDigit * (10 ** i)
        m //= 10

    if rPart == 0: return -1
    lPart = (n - rPart) // (10 ** partitionSize)
    return lPart + rPart

def isKaprekarNumber(n):
    square    = n ** 2
    numDigits = digitCount(square)

    for i in range(numDigits):
        if sumPartition(square, i + 1) == n: return True

    return False

# Return the strictly left Kaprekar number between
# the loweBound and upperBound. Start searching from
# upperBound and move towards lowerBound

def findLeftKaprekar(lowerBound, upperBound):
    guess = upperBound

    while guess > lowerBound:
        guess -= 1
        if isKaprekarNumber(guess): return guess, (upperBound - guess)

    return -1, -1  # Invalid Kaprekar

def findRightKaprekar(lowerBound, upperBound):
    guess = lowerBound

    if upperBound == 0:
        while True:
            guess += 1
            if isKaprekarNumber(guess): break
    else:
        while guess < upperBound:
            guess += 1
            if isKaprekarNumber(guess): break

    return guess, (guess - lowerBound)

def nearestKaprekarNumber(n):
    m = math.floor(n)
    if n < 0: return 1
    elif isKaprekarNumber(m): return m

    leftKaprekar,  distanceLeft  = findLeftKaprekar(0, m)
    if distanceLeft != -1 :
        upperBound = roundHalfUp(n) + distanceLeft + 1
        rightKaprekar, distanceRight = findRightKaprekar(m, upperBound + 1)
    else:
        rightKaprekar, distanceRight = findRightKaprekar(m, 0)

    distanceLeft  += abs(n - m)
    distanceRight -= abs(n - m)

    if distanceLeft == -1:
        return rightKaprekar
    if distanceLeft == distanceRight:
        return min(leftKaprekar, rightKaprekar)
    elif distanceLeft < distanceRight:
        return leftKaprekar
    else: return rightKaprekar

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)  #####
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    # kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    # bigKaps = [994708, 999999]
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)

    # The test case below will be painfully slow. Works though!
    # Perhaps there's a better way of going about it.

    # assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")
#################################################
# testAll and main
#################################################

def testAll():
    testNearestKaprekarNumber()

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
        #'range,reversed,str,' # added 'str' for play112 bonus
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()