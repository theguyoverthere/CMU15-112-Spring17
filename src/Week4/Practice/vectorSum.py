#******************************************************************************#
# Author: Tarique Anwer
# Date:   16/4/2017
# Description: vectorSum takes two same-length lists of numbers a and b, and
#              returns a new list c where c[i] is the sum of a[i] and b[i]
#              For example, vectorSum([2,4], [20,30]) returns [22, 34]
#******************************************************************************#
import cs112_s17_linter

def vectorSum(a, b):
    c = []
    for index in range(len(a)):
        c.append(a[index] + b[index])

    return c

def testVectorSum():
    print("Testing median()...", end="")
    assert(vectorSum([], []) == [])
    assert(vectorSum([1], [2]) == [3])
    assert(vectorSum([1, 2], [-1, -2]) == [0, 0])
    assert(vectorSum([1, 2, 3], [34, 40, 50]) == [35, 42, 53])
    assert(vectorSum([-1, -2], [-1, -2]) == [-2, -4])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testVectorSum()

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