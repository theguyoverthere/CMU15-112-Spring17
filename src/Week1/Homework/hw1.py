#################################################
# Hw1
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
# Hw1 problems
#################################################

def fabricYards(inches):
    return math.ceil(inches / 36)
 
def fabricExcess(inches):
    return (fabricYards(inches) * 36) - inches

def isLegalTriangle(s1,s2,s3):
    # Twice the longest side is less than the sum of the three sides combined.
    # The value on the right hand side of the expression does NOT have to be
    # the longest side. However, even if it happens to be the longest side,
    # the inequality still remains valid.
    # s1 + s2 > s3 => s1 + s2 + s3 > s3 + s3
    # s2 + s3 > s1 => s1 + s2 + s3 > s1 + s1
    # s1 + s3 > s2 => s2 + s1 + s3 > s2 + s2
    if (s1 <= 0) or (s2 <= 0) or (s3 <= 0): return False
    longestSide = max(s1, s2, s3)
    return 2 * longestSide < (s1 + s2 + s3)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x3, y3, x1, y1)

    if isLegalTriangle(s1,s2, s3):
        hypotenuse = max(s1, s2, s3)
        if math.isclose(hypotenuse, s3):
            if math.isclose((s3 ** 2), (s1 ** 2 + s2 ** 2)): return True
        elif math.isclose(hypotenuse, s2):
            if math.isclose((s2 ** 2), (s1 ** 2 + s3 ** 2)): return True
        elif math.isclose(hypotenuse, s1):
            if math.isclose((s1 ** 2), (s2 ** 2 + s3 ** 2)): return True

        return False

def extractColor(rgb, component):
    if   component == 'R':
        return rgb // (10 ** 6)
    elif component == 'G':
        return (rgb % (10 ** 6)) // (10 ** 3)
    elif component == 'B':
        return rgb % (10 ** 3)
    else:
        return 0

def colorBlender(rgb1, rgb2, midpoints, n):

    if n < 0 or n > midpoints + 1:
        return None

    nGaps = midpoints + 1

    r1 = extractColor(rgb1, 'R')
    g1 = extractColor(rgb1, 'G')
    b1 = extractColor(rgb1, 'B')

    r2 = extractColor(rgb2, 'R')
    g2 = extractColor(rgb2, 'G')
    b2 = extractColor(rgb2, 'B')

    deltaR = (r2 - r1) / nGaps
    deltaG = (g2 - g1) / nGaps
    deltaB = (b2 - b1) / nGaps

    nthR = roundHalfUp(r1 + (n * deltaR))
    nthG = roundHalfUp(g1 + (n * deltaG))
    nthB = roundHalfUp(b1 + (n * deltaB))

    return (nthR * (10 ** 6)) + (nthG * (10 ** 3)) + nthB

def bonusFindIntRootsOfCubic(a, b, c, d) :
    p = (-1) * (b / (3 * a))
    q = (p ** 3) + (((b * c) -(3 * a * d))/(6 * a * a))
    r = c / (3 * a)

    # Given one real root, the equation can be decomposed to get the form below:
    # ax^3 + bx^2 + cx + d = (x - root1)(ax^2 + (b + a * root1)x + c + b * root1 + a * root1^2)
    #Quadratic Equation: ax^2 + (b + a * root1)x + c + b * root1 + a * root1^2

    # Extract the real part of the (possibly) complex root. Ignore the imaginary part.
    root1 = ((q + (((q ** 2) + ((r - (p ** 2)) ** 3)) ** 0.5)) ** (1/3) + \
             (q - (((q ** 2) + ((r - (p ** 2)) ** 3)) ** 0.5)) ** (1/3) + p).real

    # Solve the quadratic equation for the other two roots. Again, extract the real
    # part of the complex number as z.real, where z is complex.
    aq = a
    bq = b + (a * root1)
    cq = c + (b * root1) + (a * (root1 ** 2))

    # Cannot use math.sqrt() for negative values. Use pow instead.
    root2 =  (((-1) * bq + pow(((bq ** 2) - (4 * aq * cq)),0.5)) / (2 * aq)).real
    root3 =  (((-1) * bq - pow(((bq ** 2) - (4 * aq * cq)),0.5)) / (2 * aq)).real

    # The solution is guaranteed to be integers for the exercise. Hence, round to
    # the nearest integer with ties going away from zero.
    root1 = roundHalfUp(root1)
    root2 = roundHalfUp(root2)
    root3 = roundHalfUp(root3)

    # Sort the three roots in ascending order
    rmin = min(root1, root2, root3)
    rmax = max(root1, root2, root3)
    rmid = root1 + root2 + root3 - (rmin + rmax)

    return rmin, rmid, rmax

#################################################
# Hw1 Test Functions
#################################################

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def testAll():
    testFabricYards()
    testFabricExcess()
    testIsRightTriangle()
    testColorBlender()
    testBonusFindIntRootsOfCubic()

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
