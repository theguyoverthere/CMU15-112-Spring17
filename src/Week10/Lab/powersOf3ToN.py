import math

def almostEqual(d1, d2, epsilon=10**-7):
    """ Test for equality of two floating point values, A & B by seeing if they
    are within epsilon of each other.

    :param d1: Floating Point value A.
    :param d2: Floating point value B
    :param epsilon: A very small delta.
    :return: True if the difference of the two floating point values is within
    epsilon. False, otherwise.

    """
    return abs(d2 - d1) < epsilon

def power(base, exp):
    """ Raises base to the power exp. Anything raised to 0 return 1.

    :param base: Integer base.
    :param exp: Non-negative integer exponent.
    :return: Base raised to the exponent, exp.
    """

    # Anything raised to zero(including 0), returns 1.
    if exp == 0:
        result = 1
    # Zero raised to anything, returns 0.
    elif base == 0:
        result = 0
    # Negative exponent.
    elif exp < 0:
        result = 1 / (base * power(base, abs(exp) - 1))
    # Positive exponent.
    else:
        result = base * power(base, exp - 1)

    return result

def largestPowerOf3(n):
    """ Takes a positive integer or float and returns the highest power of 3,
    up to and including n.

    :param n: A positive integer or float.
    :return: The highest power of three up to and including n. Returns None if
             no power of three exists in the given range.
    """

    try:
        return int(math.pow(3,
                            math.floor(math.log(math.floor(n)) / math.log(3))))
    except ValueError:
        return None

def powersOf3ToN(n):
    """ Takes a possibly-negative float or int n, and returns a list of the
    positive powers of 3 up to and including n, or None (not an empty list) if
    no such values exist. As an example, powersOf3ToN(10.5) returns [1, 3, 9].

    :param n: Possibly negative float or int.
    :return: Returns a list of the positive powers of 3 up to and including n,
             or None (not an empty list) if no such values exist. As an example,
             powersOf3ToN(10.5) returns [1, 3, 9].
    """
    result = []

    if n < 1:
        result = None
    else:
        currentPower = largestPowerOf3(n)
        previousPower = powersOf3ToN(n // 3)

        if currentPower: result.append(currentPower)
        if previousPower: result = result + previousPower

    if result: result.sort()
    return result
