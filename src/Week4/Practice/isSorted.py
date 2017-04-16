#******************************************************************************#
# Author: Tarique Anwer
# Date:   16/4/2017
# Description:  isSorted(a) takes a list of numbers and returns True if the list
#               is sorted (either smallest-first or largest-first) and False
#               otherwise. Your function must only consider each value in the
#               list once (so, in terms of big-oh, which we will learn soon, it
#               runs in O(n) time, where n=len(a)), and so in particular you may
#               not sort the list.
#******************************************************************************#
import cs112_s17_linter

def isSorted(a):
    equalCount      = 0
    increasingCount = 0
    decreasingCount = 0

    if len(a) == 0: return True

    for index in range(len(a) - 1):
        if a[index] == a[index + 1]:
            equalCount += 1
        elif a[index] > a[index + 1]:
            increasingCount += 1
        elif a[index] < a[index + 1]:
            decreasingCount += 1

    return ((increasingCount == len(a) - equalCount - 1) or
            (decreasingCount == len(a) - equalCount - 1))


def testIsSorted():
    print("Testing alternatingSum()...", end="")
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([-1]) == True)
    assert(isSorted([1, 1]) == True)
    assert(isSorted([-1, 0, 1]) == True)
    assert(isSorted([1, 2, 1]) == False)
    assert(isSorted([5, 3, 8, 4]) == False)
    assert(isSorted([1, 3, 4, 8]) == True)
    assert(isSorted([1, 3, 3, 4]) == True)
    assert(isSorted([1, 1, 2, 4]) == True)
    assert(isSorted([4, 4, 2, 2]) == True)
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