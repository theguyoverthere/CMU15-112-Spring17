import cs112_s17_linter
import math

def nearestOdd(n):
    if math.ceil(n) % 2 == 1 : return math.ceil(n)
    return math.ceil(n) - 1

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')

    assert(nearestOdd(-2.01) == -3)
    assert(nearestOdd(-2.50) == -3)
    assert(nearestOdd(-2.95) == -3)

    assert(nearestOdd(-1.01) == -1)
    assert(nearestOdd(-1.50) == -1)
    assert(nearestOdd(-1.95) == -1)

    assert(nearestOdd(0) == -1)

    assert(nearestOdd(1.01) == 1)
    assert(nearestOdd(1.50) == 1)
    assert(nearestOdd(1.95) == 1)

    assert(nearestOdd(1) == 1)
    assert(nearestOdd(2) == 1)
    assert(nearestOdd(3) == 3)

    assert(nearestOdd(2.01) == 3)
    assert(nearestOdd(2.50) == 3)
    assert(nearestOdd(2.95) == 3)

    assert(nearestOdd(-1) == -1)
    assert(nearestOdd(-2) == -3)
    assert(nearestOdd(-3) == -3)

    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNearestOdd()

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
