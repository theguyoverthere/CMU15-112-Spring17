#1) Buggy code that crashes (look at stack trace for clues)

# intentionally buggy code here!
def isFactor(factor, n):
    return n % factor == 0

def digitFactors(n):
    #returns the number of digits of n that are factors of n
    count = 0
    while n > 0:
        digit = n % 10
        n /= 10
        if isFactor(n, digit):
            #found another digit that divides n
            count += 1
    return count

#8 is a factor of 80, but 0 is not, so digitFactors(80) should return 1
# print (digitFactors(80)) #crashes


#2) Once again, but catching the exception to print out more information
# but we lost the stack trace!

# intentionally buggy code here!
def isFactor1(factor, n):
    return n % factor == 0

def digitFactors1(n):
    #returns the number of digits of n that are factors of n
    count = 0
    while n > 0:
        digit = n % 10
        n /= 10
        try:
            if isFactor1(n, digit):
                #found another digit that divides n
                count += 1
        except:
            print("Crashed on this input", n, digit)
    return count

#8 is a factor of 80, but 0 is not, so digitFactors(80) should return 1
# print (digitFactors1(80)) # Exits cleanly without crashing

#3) Yet again, this time explicitly printing the stack trace, and not crashing!

import traceback, sys

# intentionally buggy code here!
def isFactor2(factor, n):
    return n % factor == 0

def digitFactors2(n):
    #returns the number of digits of n that are factors of n

    count = 0
    while n > 0:
        digit = n % 10
        n /= 10
        try:
            if isFactor2(n, digit):
                #found another digit that divides n
                count += 1
        except Exception as error:
            print("Crashed on this input", n, digit)
            print("Error: ", error)
            traceback.print_exc(file=sys.stderr)
    return count

#8 is a factor of 80, but 0 is not, so digitFactors(80) should return 1
# print (digitFactors2(80)) #Does not crash, prints Stack Trace


#4) Once more, this time re-raising  the exception, so yet again crashing!

import traceback, sys

# intentionally buggy code here!
def isFactor3(factor, n):
    return n % factor == 0

def digitFactors3(n):
    #returns the number of digits of n that are factors of n

    count = 0
    while n > 0:
        digit = n % 10
        n /= 10
        try:
            if isFactor2(n, digit):
                #found another digit that divides n
                count += 1
        except Exception as error:
            # print("Crashed on this input", n, digit)
            raise
    return count

#8 is a factor of 80, but 0 is not, so digitFactors(80) should return 1
print (digitFactors3(80)) # crashes



