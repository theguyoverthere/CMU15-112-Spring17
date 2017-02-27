import cs112_s17_linter

def numConsecutiveDigits(nthDigit, n):
    numCount = 0

    while n % 10 == nthDigit:
        numCount += 1
        n //= 10
    return numCount

def longestDigitRun(n):
    n = abs(n)
    if n < 10 : return n

    prevMax          = -1  # Store the integer
    prevMaxLength    =  0  # Store the associated consecutive length.
    currentLength    =  0  # Consecutive length for the current iteration.

    while n > 0:
        nthDigit = n % 10  # Partition the integer into two parts.
        n //= 10

        currentLength = numConsecutiveDigits(nthDigit, n)

        if currentLength > prevMaxLength:
            prevMaxLength = currentLength
            prevMax       = nthDigit
        elif currentLength == prevMaxLength:
            prevMax = min(nthDigit, prevMax)

    return prevMax

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    print('Passed.')


#################################################
# testAll and main
#################################################

def testAll():
    testLongestDigitRun()

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

