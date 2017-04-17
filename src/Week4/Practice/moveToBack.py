#******************************************************************************#
# Author: Tarique Anwer
# Date:   17/4/2017
# Function: moveToBack(a,b) takes two lists a and b, and destructively modifies
#           a so that each element of a that appears in b moves to the end of a
#           in the order that they appear in b. The rest of the elements in a
#           should still be present in a, in the same order they were originally
# Args:     a: List of integers
#           b: List of integers
# Returns:  a: The modified list is returned
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def moveToBack(a, b):
    end = []

    for index in range(len(b)):
        while b[index] in a:
            element = a.pop(a.index(b[index]))
            end.append(element)

        for i in range(len(end)):
            a.append(end[i])

        end = []

    return a

def testMoveToBack():
    print("Testing alternatingSum()...", end="")
    assert(moveToBack([2, 3, 3, 4, 1, 5], [3]) == [2, 4, 1, 5, 3, 3])
    assert(moveToBack([2, 3, 3, 4, 1, 5], [2, 3]) == [4, 1, 5, 2, 3, 3])
    assert(moveToBack([2, 3, 3, 4, 1, 5], [3, 2]) == [4, 1, 5, 3, 3, 2])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testMoveToBack()

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