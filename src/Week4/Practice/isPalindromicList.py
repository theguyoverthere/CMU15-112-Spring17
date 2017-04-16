import cs112_s17_linter
#******************************************************************************#
# Author: Tarique Anwer
# Date:   9/4/2017
# Function: Takes a list and returns True if it is the same forward as
#           backward and False otherwise.
# Args:     Any list
# Returns:  True if the list is "palindromic", False otherwise
# Raises:   NA
#******************************************************************************#

def isPalindromicList(n):
    lo = 0
    hi = len(n) - 1

    while lo <= hi:
        if n[lo] != n[hi]:
            return False
        lo += 1
        hi -= 1

    return True

def testIsPalindromicList():
    print("Testing isPalindromicList()...", end="")
    assert(isPalindromicList([]) == True)
    assert(isPalindromicList([1]) == True)
    assert(isPalindromicList([-1]) == True)
    assert(isPalindromicList([1, 1]) == True)
    assert(isPalindromicList([-1, 0, 1]) == False)
    assert(isPalindromicList([1, 2, 1]) == True)
    assert(isPalindromicList([5, 3, 8, 4]) == False)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testIsPalindromicList()

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