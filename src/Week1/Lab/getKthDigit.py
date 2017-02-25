import cs112_s17_linter

def getKthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(789, 0)  == 9)
    assert(getKthDigit(789, 2)  == 7)
    assert(getKthDigit(789, 3)  == 0)
    assert(getKthDigit(-789, 0) == 9)

    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testGetKthDigit()

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

