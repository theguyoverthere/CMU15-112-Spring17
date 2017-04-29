import cs112_s17_linter
#******************************************************************************#
# Author: Tarique Anwer
# Date:   9/4/2017
# Function: Takes a list of numbers and returns the alternating sum(where
#           the sign alternates from positive to negative and vice versa).
# Args:     A List of Numbers
# Returns:  Alternating sum as an integer or a float.
# Raises:   NA
#******************************************************************************#
def alternatingSum(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * ((-1) ** i)

    return sum

def testAlternatingSum():
    print("Testing alternatingSum()...", end="")
    assert(alternatingSum([]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([-1]) == -1)
    assert(alternatingSum([1, 1]) == 0)
    assert(alternatingSum([-1, 0, 1]) == 0)
    assert(alternatingSum([1, 1, 1]) == 1)
    assert(alternatingSum([5, 3, 8, 4]) == 6)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testAlternatingSum()

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
