import cs112_s17_linter
import math

def isLegalTriangle(s1,s2,s3):
    # Twice the longest side is less than the sum of the three sides combined.
    # The value on the right hand side of the expression does NOT have to be
    # the longest side. However, even if it happens to be the longest side,
    # the inequality still remains valid.
    # s1 + s2 > s3 => s1 + s2 + s3 > s3 + s3
    # s2 + s3 > s1 => s1 + s2 + s3 > s1 + s1
    # s1 + s3 > s2 => s2 + s1 + s3 > s2 + s2
    if (s1 <= 0) or (s2 <= 0) or (s3 <= 0): return False
    longestSide = max(s1, s2, s3)
    return 2 * longestSide < (s1 + s2 + s3)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x3, y3, x1, y1)

    if isLegalTriangle(s1,s2, s3):
        hypotenuse = max(s1, s2, s3)
        if math.isclose(hypotenuse, s3):
            if math.isclose((s3 ** 2), (s1 ** 2 + s2 ** 2)): return True
        elif math.isclose(hypotenuse, s2):
            if math.isclose((s2 ** 2), (s1 ** 2 + s3 ** 2)): return True
        elif math.isclose(hypotenuse, s1):
            if math.isclose((s1 ** 2), (s2 ** 2 + s3 ** 2)): return True

        return False

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testIsRightTriangle()

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
