import cs112_s17_linter
import decimal

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def extractColor(rgb, component):
    if   component == 'R':
        return rgb // (10 ** 6)
    elif component == 'G':
        return (rgb % (10 ** 6)) // (10 ** 3)
    elif component == 'B':
        return rgb % (10 ** 3)
    else:
        return 0

def colorBlender(rgb1, rgb2, midpoints, n):

    if n < 0 or n > midpoints + 1:
        return None

    nGaps = midpoints + 1

    r1 = extractColor(rgb1, 'R')
    g1 = extractColor(rgb1, 'G')
    b1 = extractColor(rgb1, 'B')

    r2 = extractColor(rgb2, 'R')
    g2 = extractColor(rgb2, 'G')
    b2 = extractColor(rgb2, 'B')

    deltaR = (r2 - r1) / nGaps
    deltaG = (g2 - g1) / nGaps
    deltaB = (b2 - b1) / nGaps

    nthR = roundHalfUp(r1 + (n * deltaR))
    nthG = roundHalfUp(g1 + (n * deltaG))
    nthB = roundHalfUp(b1 + (n * deltaB))

    return (nthR * (10 ** 6)) + (nthG * (10 ** 3)) + nthB

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testColorBlender()

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

