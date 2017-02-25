print(" 6%3 =", (6 % 3))
print(" 5%3 =", (5 % 3))
print(" 2%3 =", (2 % 3))
print(" 0%3 =", (0 % 3))

# Modulus is the distance between the numerator and the largest multiple of the denominator which is no larger
# than the numerator.

# For the example below, the next lower multiplicand of -3 is -6. Therefore the result is the distance between
# (-4) and (-6) which is 2
print("-4%3 =", (-4 % 3))

# print(" 3%0 =", (3 % 0))


def mod(a, b):
    return a - (a//b) * b

print(41 % 14, mod(41, 14))
print(14 % 41, mod(14, 41))
print(-32 % 9, mod(-32, 9))
print(32 % -9, mod(32, -9))
