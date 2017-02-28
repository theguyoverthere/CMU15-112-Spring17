import cs112_s17_linter

def numConsecutiveDecreasingDigits(n):
    digitCount = 1
    numSequence     = 0
    
    while n > 0:
        nthDigit = n % 10
        mthDigit = (n % 100) // 10

        # We have either reached the leftmost digit or found one which is in
        # an incorrect order.
        if (mthDigit == 0) or (nthDigit <= mthDigit): break

        numSequence += nthDigit * (10 ** (digitCount - 1))
        digitCount += 1

        n //= 10

    numSequence += nthDigit * (10 ** (digitCount - 1))

    return digitCount, numSequence

  
def longestIncreasingRun(n):

    maxLength       = 0  # Store the associated consecutive length.
    longestSequence = 0  # Longest increasing sequence so far.

    while n > 0:
        currentLength   = 0 # Consecutive length for the current iteration.
        currentSequence = 0 # Value of the current sequence of increasing digits.

        currentLength, currentSequence = numConsecutiveDecreasingDigits(n)

        if currentLength > maxLength:
            maxLength       = currentLength
            longestSequence = currentSequence
            n //= (10 ** (currentLength - 1))

        elif currentLength == maxLength:
            longestSequence = max(currentSequence, longestSequence)

        n //= 10

    return longestSequence

def testLongestIncreasingRun():
    print('Testing longestIncreasingRun()... ', end='')
    assert(longestIncreasingRun(27648923679) == 23679)
    assert(longestIncreasingRun(123345) == 345)
    assert(longestIncreasingRun(1232) == 123)
    assert(longestIncreasingRun(0) == 0)
    assert(longestIncreasingRun(1) == 1)
    assert(longestIncreasingRun(10012301230123) == 123)
    assert(longestIncreasingRun(12345678987654321) == 123456789)
    print('Passed.')


#################################################
# testAll and main
#################################################

def testAll():
    testLongestIncreasingRun()

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
