#******************************************************************************#
# Author: Tarique Anwer
# Date:   16/4/2017
# Description: nondestructiveRotateList(a, n) takes a list a and an integer n,
#              and non-destructively modifies the list so that each element is
#              shifted to the right by n indices (including wraparound). The
#              function should then return this new list. True if a2 is a
#              rotation of a1 and False otherwise.
#******************************************************************************#
import cs112_s17_linter

def nondestructiveRotateList(a, n):
    if n > 0:
        return a[len(a) - n:] + a[: len(a) - n]
    else:
        return a[abs(n):] + a[:abs(n)]

def testNondestructiveRotateList():
    print("Testing nondestructiveRotateList()...", end="")
    assert(nondestructiveRotateList([1,2,3,4], 1) == [4, 1, 2, 3])
    assert(nondestructiveRotateList([4,3,2,6,5], 2) == [6, 5, 4, 3, 2])
    assert(nondestructiveRotateList([1,2,3], 0) == [1,2,3])
    assert(nondestructiveRotateList([1, 2, 3], -1) == [2, 3, 1])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testNondestructiveRotateList()

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
