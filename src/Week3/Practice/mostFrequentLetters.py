import cs112_s17_linter
import string

def maxNonZeroDigit(n):
    largestNonZeroDigit = 0

    while n > 0:
        nthDigit = n % 10

        if (nthDigit != 0) and (nthDigit > largestNonZeroDigit):
            largestNonZeroDigit = nthDigit

        n //= 10

    return largestNonZeroDigit

def mostFrequentLetters(s):
    if s == "" : return ""

    lookupString = ""
    result = ""

    for c in string.ascii_lowercase:
        lookupString += str(s.lower().count(c))

    highestFrequency = str(maxNonZeroDigit(int(lookupString)))

    for i in range(len(lookupString)):
        if lookupString[i] == highestFrequency:
            result += string.ascii_uppercase[i]

    return result

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("Cat") == 'ACT')
    assert(mostFrequentLetters("A cat") == 'A')
    assert(mostFrequentLetters("A cat in the hat") == 'AT')
    assert(mostFrequentLetters("This is a test") == 'ST')
    assert(mostFrequentLetters("This is an I test?") == 'IST')
    assert(mostFrequentLetters("") == "")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testMostFrequentLetters()

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
