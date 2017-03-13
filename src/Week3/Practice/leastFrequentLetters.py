import cs112_s17_linter
import string

def minDigit(n):
    smallestDigit = 9

    while n > 0:
        nthDigit = n % 10

        if (nthDigit != 0) and (nthDigit < smallestDigit):
            smallestDigit = nthDigit

        n //= 10

    return smallestDigit

def leastFrequentLetters(s):
    lookupString = ""
    result = ""

    for c in string.ascii_lowercase:
        lookupString += str(s.lower().count(c))

    lowestFrequency = str(minDigit(int(lookupString)))

    if lowestFrequency == 0:
        return result

    for i in range(len(s)):
        if (s[i].isalpha() and
            lookupString[ord(s[i].lower()) - ord('a')] == lowestFrequency):
            result += s[i].lower()

    return result

def testLeastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    assert(leastFrequentLetters("abc def! GFE'cag!!!") == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".lower()) == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".upper()) == "bd")
    assert(leastFrequentLetters("") == "")
    assert(leastFrequentLetters("\t \n&^#$") == "")
    noq = string.ascii_lowercase.replace('q','')
    assert(leastFrequentLetters(string.ascii_lowercase + noq) == "q")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLeastFrequentLetters()

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
