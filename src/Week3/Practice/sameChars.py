import cs112_s17_linter
import string

def compareLookupStrings(n1, n2):

    if (n1 == 0 and n2 != 0) or (n1 != 0 and n2 == 0):
        return False

    while n1 > 0 and n2 > 0:
        nthDigit1 = n1 % 10
        nthDigit2 = n2 % 10

        if (nthDigit1 * nthDigit2 == 0) and (nthDigit1 + nthDigit2 > 0):
            return False

        n1 //= 10
        n2 //= 10

    return True

def sameChars(s1, s2):
    if isinstance(s1, str) and isinstance(s2, str):
        if s1 == "" and s2 == "": return True
        else:
            lookupString1 = ""
            lookupString2 = ""

            for c in string.ascii_letters:
                lookupString1 += str(s1.count(c))
                lookupString2 += str(s2.count(c))

            return compareLookupStrings(int(lookupString1), int(lookupString2))

    return False

def testSameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("abcabcabc", "cba") == True)
    assert(sameChars("cba", "abcabcabc") == True)
    assert(sameChars("abcabcabc", "cbad") == False)
    assert(sameChars("abcabcabc", "cBa") == False)
    assert(sameChars(42,"The other parameter is not a string") == False)
    assert(sameChars("","") == True)
    assert(sameChars("","a") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testSameChars()

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
