import decimal

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def bonusFindIntRootsOfCubic(a,b,c,d) :
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

# print(bonusFindIntRootsOfCubic(5, 1, 3,  2))
# print(bonusFindIntRootsOfCubic(2, 5, 33, 7))
# print(bonusFindIntRootsOfCubic(-18, 24, 3, -8))
# print(bonusFindIntRootsOfCubic(1, 2, 3, 4))
# ax^3 + bx^2 + cx + d = 0
# ax^2 + bx  + {c  + (d/root)} = 0
# ax^2 + bx + c" = 0, c" = {c  + (d/root)}

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

testBonusFindIntRootsOfCubic()