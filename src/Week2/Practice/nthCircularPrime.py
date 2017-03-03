import cs112_s17_linter
import math

def digitCount(n):
    if n == 0: return 1

    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10

    return count

def isPrime(n):
    if n == 2:
        return True
    elif (n < 2) or (n % 2 == 0):
        return False

    for factor in range(3, math.floor(math.sqrt(n) + 1),2):
        if n % factor == 0:
            return False

    return True

def rotateNumber(n, numDigits):
    nthDigit = n % 10
    n //= 10
    n += nthDigit * (10 ** (numDigits -1))

    return n

def isCircularPrime(n):
    numDigits = digitCount(n)

    if isPrime(n):
        for i in range(numDigits):
            n = rotateNumber(n, numDigits)
            if not isPrime(n):
                return False
        return True 
    return False

def nthCircularPrime(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isCircularPrime(guess):
            found += 1
    return guess


def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(1) == 3)
    assert(nthCircularPrime(2) == 5)
    assert(nthCircularPrime(10) == 73)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(16) == 199)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNthCircularPrime()

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
