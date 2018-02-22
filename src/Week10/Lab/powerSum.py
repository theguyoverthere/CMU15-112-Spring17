#******************************************************************************#
# Author: Tarique Anwer
# Date:   16/2/2018
# Description: Write the function powerSum(n, k) that takes two possibly-
#              negative integers n and k and returns the so-called power sum:
#              1**k + 2**k + ... + n**k
#              If n is negative, return 0. Similarly, if k is negative,
#              return 0.
#******************************************************************************#

def power(base, exp):
    """ Raises base to the power exp. Anything raised to 0 return 1.

    :param base: Integer base.
    :param exp: Non-negative integer exponent.
    :return: Base raised to the exponent, exp.
    """

    if exp == 0:
        result = 1
    elif base == 0:
        result = 0
    elif exp < 0:
        result = 1 / (base * power(base, abs(exp) - 1))
    else:
        result = base * power(base, exp - 1)

    return result

def powerSum(n, k):
    """ Takes two possibly-negative integers n and k and return the power sum.
        1**k + 2**k + ... + n**k
    :param n: Maximum integer base in the sum of powers.
    :param k: Integer exponent.
    :return: Power Sum
    """

    if n <=0 or k < 0:
        result = 0
    else:
        result = power(n, k) + powerSum(n - 1, k)

    return result
