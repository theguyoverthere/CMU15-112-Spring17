import cs112_s17_linter
import math

def isPerfectNumber(n):
    if n <= 1 : return False

    divisorSum = 0

    for divisor in range(1, math.floor(n  ** 0.5) + 1):
        if n % divisor == 0:
            divisorSum += divisor
            divisorSum += (n // divisor) # Divisors appear in pairs, but we're only
                                         # picking up the one below the square root.

    # Because we're starting division at 1, we're including the pair divisor i.e.
    # n itself in the divisorSum.
    return divisorSum == 2 * n

def nthPerfectNumber(n):
    found = 0
    guess = 0
    while found  <= n:
        guess += 1
        if isPerfectNumber(guess):
            found += 1
    return guess

def testNthPerfectNumber():
    print('Testing nthPerfectNumber()... ', end='')
    assert(nthPerfectNumber(0) == 6)
    assert(nthPerfectNumber(1) == 28)
    assert(nthPerfectNumber(2) == 496)
    assert(nthPerfectNumber(3) == 8128) # this can be slow
    print('Passed.')


#################################################
# testAll and main
#################################################

def testAll():
    testNthPerfectNumber()

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