import cs112_s17_linter

def sumOfSquaresOfDigits(n):
    sumSquare = 0

    while n > 0:
        nthDigit = n % 10
        sumSquare += (nthDigit ** 2)

        n //= 10

    return sumSquare

        
def isHappyNumber(n):
    
    if   n <= 0: return False
    if   n == 1: return True  
    elif n == 4: return False # Special Case

    while True:
        if (n == 1) or (n == 4): break
        n = sumOfSquaresOfDigits(n)
    return n == 1
    
def nthHappyNumber(n):
    guess = 0
    found = -1 
    while found < n:
        guess += 1
        if isHappyNumber(guess):
            found += 1
    
    return guess

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    print("Passed.")



#################################################
# testAll and main
#################################################

def testAll():
    testNthHappyNumber()

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
