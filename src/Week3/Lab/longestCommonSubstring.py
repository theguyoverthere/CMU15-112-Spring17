import cs112_s17_linter

#Brute Force it.

def longestCommonSubstring(s1, s2):
    longestSubstring = ""
    longestSubstringLength = 0

    if len(s1) <= len(s2):
        shortString = s1
        longString  = s2
    else:
        shortString = s2
        longString  = s1

    for i in range(len(shortString)):
        for j in range(i + 1, len(shortString)):
            subString = shortString[i:j + 1]

            if longString.find(subString) > 0:
                if len(subString) == longestSubstringLength:
                    if subString < longestSubstring:
                        longestSubstring = subString

                elif len(subString) > longestSubstringLength:
                    longestSubstringLength = len(subString)
                    longestSubstring = subString

    return longestSubstring

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    testLongestCommonSubstring()

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


