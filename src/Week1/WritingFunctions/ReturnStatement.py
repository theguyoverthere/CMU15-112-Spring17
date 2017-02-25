# Basic example


def is_positive(x):
    print("Hello")
    return (x > 0)
    print("GoodBye")  # Does not run (Dead Code)

print(is_positive(5))
# print(is_positive(-5))
# print(is_positive(0))


def f(x):
    x + 42
    # return x + 42

print(f(2))


# The same function is redefined below. When the print(f(2)) is next executed, it refers to the new
# definition.


def f(x):
    result = x + 40
    # return result

print(f(2))

# Print versus return
def cubed(x):
    print(x**3)

cubed(3)             # Will print 9 because the of the print statement in the function
print(cubed(3))      # Python will add a return None statement because there isn;'t one. When that is printed,
                     # a 'None' will be printed.
# print(2 * cubed(3))  # print ALWAYS takes a String argument. What we're trying to do is to pass on an expression
                     # <string> * None, which results in an error


# Correctly defined
def cubed(x):
    return x ** 3

cubed(2)
print(cubed(2))
print(2 * cubed(2))


def hypotenuse(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5

print(hypotenuse(3, 4))
print("------------------------")


def xor(b1, b2):
    return (b1 and (not b2)) or (b2 and (not b1))

print(xor(True,  True))
print(xor(True,  False))
print(xor(False, True))
print(xor(False, False))
print("------------------------")


def is_positive(n):
    return n > 0

print(is_positive(10))
print(is_positive(-1.234))



