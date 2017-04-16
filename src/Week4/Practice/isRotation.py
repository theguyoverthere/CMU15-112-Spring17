#******************************************************************************#
# Author: Tarique Anwer
# Date:   16/4/2017
# Description: isRotation(a1, a2) that takes two lists, a1 and a2, and returns
#              True if a2 is a rotation of a1 and False otherwise.
#******************************************************************************#
import cs112_s17_linter

# position is a positive integer
def rotateListLeft(a, position):
    return a[position + 1:] + a[: position + 1]

def isRotation(a1, a2):
    if len(a1) == len(a2):
        if a1 == a2: return True

        for index in range(len(a1)):
            if a1 == rotateListLeft(a2, index):
                return True

    return False

def testIsRotation():
    print("Testing isRotation()...", end="")
    assert(isRotation([], []) == True)
    assert(isRotation([1], [1]) == True)
    assert(isRotation([1, 2], [2, 1]) == True)
    assert(isRotation([1, 2, 2, -2], [2, 2, -2, 1]) == True)
    assert(isRotation([3, 2, 0, -2], [-2, 3, 2, 0]) == True)
    assert(isRotation([43, 2, 0, -2], [-2, 43, 2]) == False)
    assert(isRotation([2,3,4,5,6], [4,5,6,2,3]) == True)
    assert(isRotation([2,3,4,5,6], [5,6,2,3,4]) == True)
    assert(isRotation([2,3,4,5,6], [6,2,3,4,5]) == True)
    assert(isRotation([2,3,4,5,6], [2,3,4,5,6]) == True)
    assert(isRotation([2,3,4,5,6], [3,4,5,6,2]) == True)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testIsRotation()

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
