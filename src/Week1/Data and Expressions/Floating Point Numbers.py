print(0.1 + 0.1 == 0.2)         # True, but..
print(0.1 + 0.1 + 0.1 == 0.3)   # False, the mask comes off!

print(0.1 + 0.1 + 0.1)          # Prints 0.30000000000000004
print((0.1 + 0.1 + 0.1) - 0.3)  # 5.551115123125783e-17 tiny but non-zero!

print("The problem")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3

#  Floating point numbers cannot be compared with the == sign due to internal
#  representation. The actual number stored in memory would be very close to the number
#  assigned, but MAY NOT be exactly equal.
print(d1 == d2)  # False

print()

print("The solution")
# epsilon = 1e-10
# print(abs(d1 - d2) < epsilon)


def almostEqual(x, y):
    epsilon = 1e-10
    return abs(x - y) < epsilon

print(almostEqual(d1, d2))


