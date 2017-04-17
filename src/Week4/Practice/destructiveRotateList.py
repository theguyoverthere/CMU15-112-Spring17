#******************************************************************************#
# Author: Tarique Anwer
# Date:   17/4/2017
# Description: This function works the same as the previous function,
#              i.e. nondestructiveRotateList only here it is destructive. That
#              is, it directly changes the list a, so after the call, that exact
#              list is rotated n indices to the right with wraparound, and a new
#              list is not created. As usual for destructive functions, this
#              function returns None. Also: you may not call the nondestructive
#              version here, and in fact, you may not even create a new list
#              (or tuple or other similar data structure) that is longer than 2
#              elements! While you must be space-efficient here, we do not
#              expect the most time-efficient approach; anything reasonable
#              (for 15-112) will do.
# Args:     List a, Integer n
# Returns:  None
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def destructiveRotateList(a, n):
    for index in range(n):
        item = a.pop(len(a) - 1)
        a.insert(0, item)

def testDestructiveRotateList():
    print("Testing alternatingSum()...", end="")
    a = [4,3,2,6,5]
    destructiveRotateList(a, 2)
    assert(a == [6, 5, 4, 3, 2])

    b = []
    destructiveRotateList(a, 0)
    assert(b == [])

    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testDestructiveRotateList()

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
