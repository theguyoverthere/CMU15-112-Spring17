#******************************************************************************#
# Author: Tarique Anwer
# Date:   18/4/2017
# Description: Takes a list and a delimiter and returns the string composed of
#              each element in the list separated by the delimiter. So,
#              join(["ab", "cd", "efg"], ",") returns "ab,cd,efg". Do not use
#              the built-in join function.
# Args:        L: List of strings
#              delimiter: delimiter for joining strings in the list.
# Returns:     Strings.
# Raises:      NA
#******************************************************************************#
import cs112_s17_linter

def join(L, delimiter):
    result = ""

    for index in range(len(L)):
        result += L[index] + delimiter

    return result[:len(result) - 1]

def testJoin():
    print("Testing join()...", end="")
    assert(join([""],',') == "")
    assert(join(["ab", "cd", "efg"], ",") == "ab,cd,efg")
    assert(join(["ab;cd;efg", "hij"], ",") == "ab;cd;efg,hij")
    assert(join(["Hello World!"],',') == "Hello World!")
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testJoin()

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
