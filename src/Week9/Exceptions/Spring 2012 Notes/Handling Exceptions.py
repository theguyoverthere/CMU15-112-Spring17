# Simplest Form
#----------------
print("1. Simplest Form")
print("----------------")
def isFactor(factor, n):
    return n % factor == 0

try:
    if isFactor(0, 2):
        print("0 is a factor of 2") # Will cause divide by zero error!
    if isFactor(2, 0):
        print("2 is a factor of 0!") # Will not be executed!
except:
    print("We just caught an error!")



# With Exception Information
#---------------------------
print(" ")
print("2. With Exception Information")
print("--------------------------")

try:
    if isFactor(0, 2):
        print("0 is a factor of 2") # Will cause divide by zero error!
    if isFactor(2, 0):
        print("2 is a factor of 0!") # Will not be executed!
except Exception as error:
    print("We just caught this error: ", error)


# Catching specific exception types
#----------------------------------
print(" ")
print("3. Catching specific exception types")
print("------------------------------------")
try:
    prompt = "Enter a number to invert:"
    n = float(input(prompt)) # non-float => ValueError
    inverse = 1 / n          # n == 0 => ZeroDivisionError
    if n == 42:
        ruhRoh()             # No such function!
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("You did not enter a number!")
except Exception as error:
    print("Unknown error:", error)
    print("   Error type:", type(error))
