#******************************************************************************#
# Author: Tarique Anwer
# Date:   9/4/2017
# Description: Non-destructive function that takes a list of floats and returns
#              the median value, which is the middle element, or the average of
#              the two middle elements. If the list is empty, return None.
#******************************************************************************#
import cs112_s17_linter
import decimal

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def median(a):
    if len(a) == 0: return None

    #Odd number of elements, hence return the middle element.
    midElement = int(roundHalfUp(len(a) / 2)) - 1

    if len(a) % 2 == 1:
        return a[midElement]
    else:
        return (a[midElement] + a[midElement + 1]) / 2

def testMedian():
    print("Testing median()...", end="")
    assert(median([]) == None) #is None
    assert(median([1]) == 1)
    assert(median([1, 2]) == 1.5)
    assert(median([1, 2, 3]) == 2)
    assert(median([1, -2, 3]) == -2)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testMedian()

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