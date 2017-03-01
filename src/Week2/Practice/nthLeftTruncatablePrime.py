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
        return True #Special Case
    elif (n < 2) or (n % 2 == 0):
        return False

    for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
        if n % factor == 0:
            return False

    return True

def nthLeftTruncatablePrime(n):
    found =  0
    guess =  1

    # Keep iterating and each time a Prime is found, make note of it.
    # Once the nth, value is found, return the guess.

    while found <= n:
        guess += 1
        numDigits = digitCount(guess)

        if isPrime(guess):
            g = guess

            while g > 0:
                lDigit = g // (10 ** (numDigits - 1))
                g -= (lDigit * (10 ** (numDigits - 1)))
                numDigits -= 1

                if (g > 0) and (not isPrime(g)): break

            if g == 0 : found += 1
    return guess

def testNthLeftTruncatablePrime():
    print('Testing nthLeftTruncatablePrime()... ', end='')
    assert(nthLeftTruncatablePrime(0) == 2)
    assert(nthLeftTruncatablePrime(10) == 53)
    assert(nthLeftTruncatablePrime(1) == 3)
    assert(nthLeftTruncatablePrime(5) == 17)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNthLeftTruncatablePrime()

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
