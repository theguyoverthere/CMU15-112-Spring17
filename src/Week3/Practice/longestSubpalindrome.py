import cs112_s17_linter

def isPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i -1]:
            return False
    return True

#Brute Force it.
def longestSubpalindrome(s):
    if isPalindrome(s):
        return s

    longestPalindrome = ""
    palindromeLength = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i : j]

            if isPalindrome(substring):
                if len(substring) == palindromeLength:
                    if substring > longestPalindrome:
                        longestPalindrome = substring
                elif len(substring) > palindromeLength:
                    longestPalindrome = substring
                    palindromeLength = j - i

    return longestPalindrome

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    testLongestSubpalindrome()

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

