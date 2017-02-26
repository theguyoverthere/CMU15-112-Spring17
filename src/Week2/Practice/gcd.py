import cs112_s17_linter

# Recursive
def gcd(m, n):
    # Euclid's theorem : gcd(x, y) = gcd(y, x % y)
    if (n == 0) : return m
    else : return gcd(n, m % n)
    return 0


# Non-Recursive
def gcd(m, n):
    # Euclid's theorem : gcd(m, n) = gcd(n, m % n)

    while (n > 0):
        mOld = m
        m = n
        n = mOld % n

    return m

# Non-recursive but cleaner IMO
def gcd(m, n):
    # Euclid's theorem : gcd(m, n) = gcd(n, m % n)

    while (n > 0):
        m, n = n, m % n  # Everything on the right is computed BEFORE the assignment
                         # takes place.
    return m


def testGcd():
    print('Testing gcd()... ', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed.')


#################################################
# testAll and main
#################################################

def testAll():
    testGcd()

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
