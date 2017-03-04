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

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

# Original: 8712, 9801, 87912, 98901, 879912
# Reversed: 2178, 1089, 21978, 10989, 219978
def reverseNumber(n):
    exponent = numDigits = digitCount(n)
    reversedNum = 0

    for i in range(numDigits):
        nthDigit = n % 10
        n //= 10
        reversedNum += nthDigit * (10 ** (exponent - 1))
        exponent -= 1


    return reversedNum

def isEmirpsPrime(n):
    return isPrime(n) and (reverseNumber(n) != n) and isPrime(reverseNumber(n))

def nthEmirpsPrime(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if isEmirpsPrime(guess):
            found += 1
    return guess

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()... ', end='')
    assert(nthEmirpsPrime(0) == 13)
    assert(nthEmirpsPrime(5) == 73)
    assert(nthEmirpsPrime(10) == 149)
    assert(nthEmirpsPrime(20) == 701)
    assert(nthEmirpsPrime(30) == 941)
    print('Passed.')


#################################################
# testAll and main
#################################################

def testAll():
    testNthEmirpsPrime()

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