import cs112_s17_linter

def setKthDigit(n, k, d):

    # As an example, replace 6 in the number below, with 5.
    # n = 12345 |6| 78901
    #Break the number into two parts using (abs(n) % (10 ** (k + 1))
    # remainder = 678901
    # n - remainder = 12345 000000
    # Divide 678901 into two parts as 6 | 78901
    # remainder2 = 78901
    # New Number = 12345 000000 + 78901 + (5 * 100000)

    # remainder = (abs(n) % (10 ** (k + 1)))
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))=
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    remainder = (abs(n) % (10 ** (k + 1)))
    result    = (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    if n < 0 : result *= -1
    return result


def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(-468, 0, 1) == -461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testSetKthDigit()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()                                      # Uncomment to enable test!

if __name__ == '__main__':
    main()
