#******************************************************************************#
# Author: Tarique Anwer
# Date:   23/4/2017
# Function: Takes a function f and a list a, and returns a new list containing
#           f(x) for each value x in a. For example, say you defined a function
#           plus3(x) that returns (x+3). Then, map(plus3, [2,4,7])
#           returns [5,7,10].
# Args:     f: A function
#           a: A list
# Returns:  A list containing f(x) for each x in a.
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def map(f, a):
    result = []

    for i in range(len(a)):
        result.append(f(a[i]))

    return result

def plus3(x):
    return x + 3

def plus4(x):
    return x + 4

def testMap():
    print("Testing alternatingSum()...", end="")
    assert(map(plus3, [1, 2, 3]) == [4, 5, 6])
    assert(map(plus4, [1, 2, 3]) == [5, 6, 7])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testMap()

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
        'list,locals,memoryview,next,object,oct,' +
        'open,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()

