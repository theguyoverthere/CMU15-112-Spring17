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

def isPalindrome(n):
    numDigits = digitCount(n)

    while n > 0:
        rDigit = n % 10
        lDigit = n // (10 ** (numDigits - 1))
        
        if rDigit != lDigit: return False

        #Truncate leftmost digit followed by the rightmost digit
        n -= lDigit * (10 ** (numDigits - 1))
        n //= 10
        numDigits-= 2

    return True


def nthPalindromicPrime(n):
    found = -1 
    guess = 1
    while found  < n:
        guess += 1
        if isPrime(guess) and isPalindrome(guess):
            found += 1
    return guess

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()... ', end='')
    assert(nthPalindromicPrime(0) == 2)
    assert(nthPalindromicPrime(1) == 3)
    assert(nthPalindromicPrime(5) == 101)
    assert(nthPalindromicPrime(10) == 313)
    print('Passed.')


#################################################
# testAll and main
#################################################

def testAll():
    testNthPalindromicPrime()

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