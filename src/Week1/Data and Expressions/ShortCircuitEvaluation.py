def yes():
    return True


def no():
    return False


def crash():
    return 1/0  #Crashes

print(no() and crash())   # Works!
# print(crash() and no)     # Crashes!
# print(yes() and crash())  # Never runs(due to crash), but would also crash without short-circuiting


print(yes() or crash())   # Works!
# print(crash() or yes())   # Crashes!
# print(no() or crash())    # Never runs(due to crash), but would also crash without short-circuiting


def isPositive(n):
    result = (n > 0)
    print("isPositive(",n,")=", result)
    return result

def isEven(n):
    result = (n %2 == 0)
    print("isEven(",n,")=", result)
    return result

print("Test1: isEven(-4) and isPositive(-4)")
print(isEven(-4) and isPositive(-4))  # Calls both functions
print("-----")
print("Test1: isEven(-3) and isPositive(-3)")
print(isEven(-3) and isPositive(-3))  # Calls only one function!