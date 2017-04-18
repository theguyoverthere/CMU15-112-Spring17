#******************************************************************************#
# Author: Tarique Anwer
# Date:   18/4/2017
# Description: Takes a list of integers and returns the smallest absolute
#              difference between any two integers in the list. If the list is
#              empty, return -1.
# Args:        List a
# Returns:     The smallest absolute difference between any two integers in the
#              list. If the list is empty, -1
# Raises:      NA
#******************************************************************************#
import cs112_s17_linter
import math

def smallestDifference(a):
    if len(a) == 0: return -1

    a.sort()
    minimumDifference = math.inf

    for index in range(len(a) - 1):
        if abs(a[index] - a[index + 1]) < minimumDifference:
            minimumDifference = abs(a[index] - a[index + 1])

    return minimumDifference

def testBinaryListToDecimal():
    print("Testing binaryListToDecimal()...", end="")
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([-7, 0]) == 7)
    assert(smallestDifference([3, -7, 0]) == 3)
    assert(smallestDifference([1, 1, 1]) == 0)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testBinaryListToDecimal()

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