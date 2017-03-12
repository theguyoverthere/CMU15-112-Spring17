import cs112_s17_linter
import string

def rotateStringRight(s, k):
    k %= len(s)

    leftSplit = s[:-k]
    rightSplit = s[-k:]

    return rightSplit + leftSplit

def testRotateStringRight():
    print("Testing rotateStringRight()...", end="")
    assert(rotateStringRight("abcde", 0) == "abcde")
    assert(rotateStringRight("abcde", 1) == "eabcd")
    assert(rotateStringRight("abcde", 2) == "deabc")
    assert(rotateStringRight("abcde", 3) == "cdeab")
    assert(rotateStringRight("abcde", 4) == "bcdea")
    assert(rotateStringRight("abcde", 5) == "abcde")
    assert(rotateStringRight("abcde", 25) == "abcde")
    assert(rotateStringRight("abcde", 28) == "cdeab")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testRotateStringRight()

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

