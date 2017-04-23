#******************************************************************************#
# Author: Tarique Anwer
# Date:   22/4/2017
# Function: firstNEvenFibonacciNumbers(n) takes a non-negative number n and
#           returns a list of the first n even Fibonacci numbers in increasing
#           order. For example, firstNEvenFibonacciNumbers(4) returns
#           [2, 8, 34, 144].
#           Must run in O(n) time, so it cannot repeatedly call
#           nthEvenFibonacciNumber.
# Args:     n: Non-Negative integer
# Returns:  List of first n even FibonacciNumbers
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter
import decimal
import math

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def nthFibonacciNumber(n):
    if (n == 0) or (n == 1): return 1

    n += 1
    phiPos = (1 + math.sqrt(5))
    phiNeg = (1 - math.sqrt(5))

    return roundHalfUp(((phiPos ** n) - (phiNeg ** n)) /
                       (math.sqrt(5) * (2 ** n)))

def firstNEvenFibonacciNumbers(n):
    result = []
    count = i = 0

    while count < n:
        currentFibonacciNumber = nthFibonacciNumber(i)
        if currentFibonacciNumber % 2 == 0:
            result.append(currentFibonacciNumber)
            count += 1
        i += 1

    return result

def testMostAnagrams():
    print("Testing alternatingSum()...", end="")
    assert (firstNEvenFibonacciNumbers(0) == [])
    assert (firstNEvenFibonacciNumbers(1) == [2])
    assert (firstNEvenFibonacciNumbers(2) == [2, 8])
    assert (firstNEvenFibonacciNumbers(3) == [2, 8, 34])
    assert (firstNEvenFibonacciNumbers(4) == [2, 8, 34, 144])
    assert (firstNEvenFibonacciNumbers(5) == [2, 8, 34, 144, 610])
    assert (firstNEvenFibonacciNumbers(6) == [2, 8, 34, 144, 610, 2584])
    assert (firstNEvenFibonacciNumbers(7) == [2, 8, 34, 144, 610, 2584, 10946])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testMostAnagrams()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,repr,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()


