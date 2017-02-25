import math

#############################################################
# Category	    Operators
# Arithmetic	+, -, *, /, //, **, %, - (unary), + (unary)
# Relational	<, <=, >=, >, ==, !=
# Assignment	+=, -=, *=, /=, //=, **=, %=, <<=, >>=
# Logical	    and, or, not
#############################################################

print(7/4)       # Floating point Division
print(7//4)      # Integer Division (Doesn't truncate but takes the math.floor value)
print(int(7/4))  # Truncate the Floating Point Division

print(-7/4)
print(-7//4)
print(int(-7/4))

# Integer Division is the same as math.floor function applied on the operands.
print((-7//4) == math.floor(-7/4))

print(7.0 // 3)
print(-7.0 // 3)

print(7.0 // 3.0)
print(-7.0 // 3.0)
