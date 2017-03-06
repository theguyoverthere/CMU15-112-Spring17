import cs112_s17_linter

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def carrylessAdd(x, y):
    nxDigits = digitCount(x)
    nyDigits = digitCount(y)
    carryLessSum = 0

    for i in range(max(nxDigits, nyDigits)):
        nthDigitX = x % 10
        nthDigitY = y % 10

        nthDigitS = nthDigitX + nthDigitY
        if nthDigitS >= 10: nthDigitS %= 10

        carryLessSum += nthDigitS * (10 ** i)
        x //= 10
        y //= 10

    return carryLessSum

def carrylessMultiply(x, y):
    previousRunningSum = 0
    numDigits = digitCount(y)

    for i in range(numDigits):
        nthDigits = y % 10
        rowSum    = 0

        for j in range(nthDigits):
            carryLessSum = carrylessAdd(rowSum, x)
            rowSum = carryLessSum

        rowSum *= (10 ** i)

        runningSum = carrylessAdd(rowSum, previousRunningSum)
        previousRunningSum = runningSum
        y //= 10

    return runningSum

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testCarrylessMultiply()

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

