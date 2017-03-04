import cs112_s17_linter

def hasEveryDigit(n):
    digit0Present = False
    digit1Present = False
    digit2Present = False
    digit3Present = False
    digit4Present = False
    digit5Present = False
    digit6Present = False
    digit7Present = False
    digit8Present = False
    digit9Present = False

    while n > 0:
        nthDigit = n % 10
        if   nthDigit == 0: digit0Present = True
        elif nthDigit == 1: digit1Present = True
        elif nthDigit == 2: digit2Present = True
        elif nthDigit == 3: digit3Present = True
        elif nthDigit == 4: digit4Present = True
        elif nthDigit == 5: digit5Present = True
        elif nthDigit == 6: digit6Present = True
        elif nthDigit == 7: digit7Present = True
        elif nthDigit == 8: digit8Present = True
        elif nthDigit == 9: digit9Present = True

        n //= 10

    return digit0Present and digit1Present and \
           digit2Present and digit2Present and \
           digit3Present and digit4Present and \
           digit5Present and digit6Present and \
           digit7Present and digit8Present and \
           digit9Present

def hasProperty309(n):
    return hasEveryDigit(n ** 5)

def nthWithProperty309(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if hasProperty309(guess):
            found += 1

    return guess


def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(5) == 635)
    assert(nthWithProperty309(6) == 662)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNthWithProperty309()

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



