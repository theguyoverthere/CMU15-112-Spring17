print("Precedence")
print(2 + 3 * 4)   # (2 + (3 * 4))    * has higher precedence than +
print(5 + 4 % 3)   # ( 5 + ( 4 % 3))  % has higher precedence than +
print(2 ** 3 * 4)  # ((2 **3 ) * 4)   ** has higher precedence than *

print()

print("Associativity")
print(5 - 3 - 4)    # ((5 - 3) - 4)   - Left to right
print(4 ** 3 ** 2)  # (4 ** (3 ** 2)) - Right to Left

print(4 ** (3 ** 2))
