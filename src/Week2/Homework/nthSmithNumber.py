import cs112_s17_linter
import math

def isPrime(n):
    if n == 2:
        return True
    elif (n < 2) or (n % 2 == 0):
        return False

    for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
        if n % factor == 0:
            return False
    return True

def isPrimeFactor(m, n):
    return isPrime(n) and m % n == 0

def digitSum(n):
    sumOfDigits = 0

    while n > 0:
        nthDigit = n % 10
        sumOfDigits += nthDigit
        n //= 10

    return sumOfDigits

def isSmithNumber(n):
    if isPrime(n) : return False
    factorDigitSum = 0
    m = n

    for factor in range(2, math.floor(n / 2) + 1):
        if m == 1: break

        if isPrimeFactor(n, factor):
            highestPower = 0

            while True:
                if m == 1 or m % factor != 0: break
                highestPower += 1
                m //= factor

            factorDigitSum += highestPower * digitSum(factor)

    return factorDigitSum == digitSum(n)

def nthSmithNumber(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if isSmithNumber(guess):
            found += 1

    return guess


def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNthSmithNumber()

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
        #'range,reversed,str,' # added 'str' for play112 bonus
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()



