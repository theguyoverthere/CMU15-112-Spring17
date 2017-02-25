import cs112_s17_linter
import math

def isPerfectSquare(n):
    if isinstance(n, int) and\
       (n >= 0)           and \
            (math.floor(math.sqrt(n)) ** 2 == n) : return True
    return False


def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')

    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(2) == False)
    assert(isPerfectSquare(2.25454) == False)
    assert(isPerfectSquare(4) == True)
    assert(isPerfectSquare(-4) == False)
    # Dicey Case but assignment says input should be int
    assert(isPerfectSquare(4.0) == False)
    assert(isPerfectSquare("Yikes!") == False)

    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testIsPerfectSquare()

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
