#1) Unnecessary raise

# def isFactor(factor, n):
#     if factor == 0:
#         raise Exception("Cannot divide by 0!") #wrong!
#     return n % factor == 0

#2) Here's why

# def isFactor(factor, n):
#     return n % factor == 0
#
# print(isFactor(0, 8))

#3) But you may use assert here, if this violates a pre-condition
#   (which it presumably does)

def isFactor(factor, n):
    assert(factor != 0)
    return n % factor == 0

print (isFactor(0, 8))