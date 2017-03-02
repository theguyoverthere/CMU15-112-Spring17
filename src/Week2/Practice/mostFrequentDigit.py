import cs112_s17_linter

def countDigitOccurrence(n, digit):
    digitCount = 0

    while n > 0:
        nthDigit = n % 10

        if nthDigit == digit:
            digitCount += 1

        n //= 10

    return digitCount

def mostFrequentDigit(n):
    if n == 0: return 0 # Special Case.

    n = abs(n)
    m = n

    maxCount      = 0
    maxCountDigit = -1
    currentCount  = 0
    while n > 0:
        nthDigit = n % 10
        currentCount = countDigitOccurrence(m, nthDigit)

        if currentCount > maxCount:
            maxCount = currentCount
            maxCountDigit = nthDigit
        elif currentCount == maxCount:
            maxCountDigit = min(nthDigit, maxCountDigit)

        n //= 10
    return maxCountDigit
    

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()... ', end='')
    assert(mostFrequentDigit(0) == 0)
    assert(mostFrequentDigit(1223) == 2)
    assert(mostFrequentDigit(12233) == 2)
    assert(mostFrequentDigit(-112233) == 1)
    assert(mostFrequentDigit(1223322332) == 2)
    assert(mostFrequentDigit(123456789) == 1)
    assert(mostFrequentDigit(1234567789) == 7)
    assert(mostFrequentDigit(1000123456789) == 0)
    print('Passed.')



#################################################
# testAll and main
#################################################

def testAll():
    testMostFrequentDigit()

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
        #'range,reversed,'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()