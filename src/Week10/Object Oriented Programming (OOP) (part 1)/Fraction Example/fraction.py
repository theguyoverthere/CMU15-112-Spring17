# Very simple, far-from-fully implemented Fraction class
# to demonstrate the OOP ideas from above.
# Note that Python actually has a full Fraction class that
# you would use instead (from fractions import Fraction),
# so this is purely for demonstrational purposes.

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

class Fraction(object):
    def __init__(self, num, den):
        # Partial implementation -- does not deal with 0 or negatives, etc
        g = gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __repr__(self):
        return "%d/%d" % (self.num, self.den)

    def __eq__(self, other):
        return (isinstance(other, Fraction) and
                (self.num == other.num) and
                (self.den == other.den))

    def __hash__(self):
        return hash(self.getHashables())

    def getHashables(self):
        return self.num, self.den

    def times(self, other):
        if isinstance(other, int):
            return Fraction(self.num * other, self.den)
        else:
            return Fraction(self.num * other.num, self.den * other.den)

def testFractionClass():
    print('Testing Fraction class...', end='')

    # Convert to String
    assert(str(Fraction(2, 3)) == '2/3')
    assert(str([Fraction(2, 3)]) == '[2/3]')

    # Test for equality
    assert(Fraction(2,3) == Fraction(2,3))
    assert(Fraction(2,3) != Fraction(2,5))
    assert(Fraction(2,3) != "Don't crash here!")

    # Test for Fraction Multiplication
    assert(Fraction(2,3).times(Fraction(3,4)) == Fraction(1,2))
    assert(Fraction(2,3).times(5) == Fraction(10,3))

    # Fraction in Sets
    s = set()
    assert(Fraction(1, 2) not in s)
    s.add(Fraction(1, 2))
    assert(Fraction(1, 2) in s)
    s.remove(Fraction(1, 2))
    assert(Fraction(1, 2) not in s)

    print('Passed.')

if __name__ == '__main__':
    testFractionClass()
