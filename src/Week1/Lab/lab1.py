#################################################
# Lab1
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
# Lab1 problems
#################################################

def nearestOdd(n):
    if math.ceil(n) % 2 == 1 : return math.ceil(n)
    return math.ceil(n) - 1

def rectanglesOverlap(x1, y1, w1, h1,
                      x2, y2, w2, h2):
    return ((x2 >= (x1 - w2)) and (x2 <= (x1 + w1)) and
            (y2 >= (y1 - h2)) and (y2 <= (y1 + h1)))


def isPerfectSquare(n):
    if isinstance(n, int) and\
       (n >= 0)           and \
            (math.floor(math.sqrt(n)) ** 2 == n) : return True
    return False

def getKthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

def setKthDigit(n, k, d):

    # As an example, replace 6 in the number below, with 5.
    # n = 12345 |6| 78901
    #Break the number into two parts using (abs(n) % (10 ** (k + 1))
    # remainder = 678901
    # n - remainder = 12345 000000
    # Divide 678901 into two parts as 6 | 78901
    # remainder2 = 78901
    # New Number = 12345 000000 + 78901 + (5 * 100000)

    # remainder = (abs(n) % (10 ** (k + 1)))
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))=
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    remainder = (abs(n) % (10 ** (k + 1)))
    result    = (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    if n < 0 : result *= -1
    return result

def boatVelocity(totalTime, upstreamDistance, riverCurrent):

    return (upstreamDistance/ totalTime) + \
           math.sqrt(((upstreamDistance / totalTime) ** 2) + (riverCurrent ** 2))

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):

    upstreamDistance = totalDistance / 2
    relativeVelocity = boatVelocity(totalTime, upstreamDistance, riverCurrent) - riverCurrent

    return upstreamDistance / relativeVelocity

#################################################
# Lab1 Test Functions
################################################

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testRiverCruiseUpstreamTime():
    print('Testing riverCruiseUpstreamTime()... ', end='')
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.7888736053508778)) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.5))
    assert(almostEqual(riverCruiseUpstreamTime(4,56,2),2.2801098892805185))
    print('Passed.')

#################################################
# Lab1 Main
################################################

def testAll():
    testNearestOdd()
    testRectanglesOverlap()
    testIsPerfectSquare()
    testGetKthDigit()
    testSetKthDigit()
    testRiverCruiseUpstreamTime()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
