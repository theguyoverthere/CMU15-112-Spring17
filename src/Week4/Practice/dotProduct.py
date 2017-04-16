#******************************************************************************#
# Author: Tarique Anwer
# Date:   16/4/2017
# Description:  This function takes two lists and non-destructively returns the
#               dotProduct of those lists. If the lists are not equal length,
#               ignore the extra elements in the longer list. Example: The 'dot
#               product' of the lists [1,2,3] and [4,5,6] is (1*4)+(2*5)+(3*6),
#               or 4+10+18, or 32
#******************************************************************************#
import cs112_s17_linter

def dotProduct(a, b):
    length = min(len(a), len(b))
    sum = 0

    for index in range(length):
        sum += a[index] * b[index]

    return sum

def testIsSorted():
    print("Testing alternatingSum()...", end="")
    assert(dotProduct([], []) == 0)
    assert(dotProduct([], [1, 2, 3]) == 0)
    assert(dotProduct([1], [1]) == 1)
    assert(dotProduct([1], [1, 2]) == 1)
    assert(dotProduct([1, 2], [1, 2, 3, 4, 5]) == 5)
    assert(dotProduct([-1, -2, 0], [1, 2, 3, 4, 5]) == -5)
    assert(dotProduct([1, 2, 3], [1, 2, 3, 4, 5]) == 14)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testIsSorted()

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
