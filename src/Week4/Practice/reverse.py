import cs112_s17_linter
#******************************************************************************#
# Author: Tarique Anwer
# Date:   9/4/2017
# Function: Destructively reverse a list. So if a equals [2, 3, 4], then after
#           reverse, a should equal [4, 3, 2]. As is generally true of
#           destructive functions, this function does not return a value.
# Args:     A list.
# Returns:  None
# Raises:   NA
#******************************************************************************#

def reverse(a):
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        a[hi], a[lo] = a[lo], a[hi]
        lo += 1
        hi -= 1

def testReverse():
    print("Testing reverse(a)...", end="")
    a = []
    reverse(a)
    assert(a == [])

    a= [1, 2, 3]
    reverse(a)
    assert(a == [3, 2, 1])

    a = ["hi", "there", 1, 2, 3]
    reverse(a)
    assert(a == [3, 2, 1, "there", "hi"])

    a = [[1,2], [2,3], [3,4]]
    reverse(a)
    assert(a == [[3,4], [2,3], [1,2]])

    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testReverse()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,repr' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()

