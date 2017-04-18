#******************************************************************************#
# Author: Tarique Anwer
# Date:   18/4/2017
# Description: Takes a string and a delimiter and returns a list of substrings
#              that are determined by that delimiter. For example,
#              split("ab,cd,efg", ",") returns ["ab", "cd", "efg"]. Do not use
#              the built-in split function.
# Args:        s: String
#              delimiter: Character, which is used to delimit the string.
# Returns:     A list of strings.
# Raises:      NA
#******************************************************************************#
import cs112_s17_linter

def split(s, delimiter):
    lo = 0
    hi = s.find(delimiter, lo)
    result = []

    while hi > 0:
        substring = s[lo : hi]
        result.append(substring)
        lo = hi + 1
        hi = s.find(delimiter, lo)

    result.append(s[lo:])

    return result

def testSplit():
    print("Testing split()...", end="")
    assert(split("",',') == [""])
    assert(split("ab,cd,efg", ",") == ["ab", "cd", "efg"])
    assert(split("ab;cd;efg,hij", ",") == ["ab;cd;efg", "hij"])
    assert(split("Hello World!",',') == ["Hello World!"])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testSplit()

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
