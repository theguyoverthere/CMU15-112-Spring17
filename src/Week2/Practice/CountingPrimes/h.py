import cs112_s17_linter

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def h(n):
    if n <= 0: return 0
    harmonicSum = 0.0

    for i in range(1, n + 1):
        harmonicSum += (1/i)

    return harmonicSum

def testH():
    print('Test h()...', end='')
    assert(almostEqual(h(0),0.0))
    assert(almostEqual(h(1),1/1.0                ))  # h(1) = 1/1
    assert(almostEqual(h(2),1/1.0 + 1/2.0        ))  # h(2) = 1/1 + 1/2
    assert(almostEqual(h(3),1/1.0 + 1/2.0 + 1/3.0))  # h(3) = 1/1 + 1/2 + 1/3
    print('Passed')

#################################################
# testAll and main
#################################################

def testAll():
    testH()

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
