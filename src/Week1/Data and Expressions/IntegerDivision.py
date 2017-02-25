import math

print("The / operator does 'normal' float division:")
print(" 5/3  =", ( 5/3))
print()
print("The // operator does integer division:")
print(" 5//3 =", (5//3))
print(" 2//3 =", (2//3))
print("-1//3 =", (-1//3))
print("-4//3 =", (-4//3))

# Integer Division is the same as math.floor function applied on the operands.
# Return the floor of x as a float, the largest integer value less than or equal to x.
# The math.floor() always returns the closest lower integer value.

# -7/4 = -1.75. Therefore the integer which is closest to -1.75 and LOWER than it, is -2
print((-7//4) == math.floor(-7/4))
