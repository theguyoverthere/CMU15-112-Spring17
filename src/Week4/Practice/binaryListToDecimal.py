#******************************************************************************#
# Author: Tarique Anwer
# Date:   18/4/2017
# Description: Takes a list of 1s and 0s, and returns the integer represented by
#              reading the list from left to right as a single binary number.
# Args:     List a
# Returns:  Integer which is the decimal representation of the 'binary list'
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def binaryListToDecimal(a):
    decimalValue = 0
    for index in range(len(a)):
        decimalValue += a[index] * (2 ** (len(a) - index - 1))

    return decimalValue

def testBinaryListToDecimal():
    print("Testing binaryListToDecimal()...", end="")
    assert(binaryListToDecimal([]) == 0)
    assert(binaryListToDecimal([0, 0]) == 0)
    assert(binaryListToDecimal([1, 0]) == 2)
    assert(binaryListToDecimal([1, 0, 1, 1]) == 11)
    assert(binaryListToDecimal([1, 1, 0, 1]) == 13)
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