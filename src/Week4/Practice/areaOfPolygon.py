#******************************************************************************#
# Author: Tarique Anwer
# Date:   30/4/2017
# Description: Write the function areaOfPolygon(L) that takes a list of (x,y)
#              points that are guaranteed to be in either clockwise or
#              counter-clockwise order around a polygon, and returns the area of
#              that polygon, as described here. For example (taken from that
#              text), areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]) returns 45.5
#              (at least the result is almostEqual to 45.5).
#******************************************************************************#
import cs112_s17_linter

def almostEqual(x, y):
    """ Helper function for comparing two floating point numbers.
    :param x: Floating point number 1
    :param y: Floating point number 2
    :return: Boolean, stating if the two numbers are "Almost equal" i.e. there
            is a difference of at most epsilon (1e-10) between the two.
    """
    epsilon = 1e-10
    return abs(x - y) < epsilon

def areaOfPolygon(L):
    """ Takes a list of (x,y) points that are guaranteed to be in either
    clockwise or counter-clockwise order around a polygon, and returns the area
    of the polygon.

    :param L: A list of (x,y) coordinates of a polygon, listed in clockwise or
              counter-clockwise direction.
    :return: Area of the polygon as a floating point number.
    """

    area = 0

    for i in range(len(L)):
        if i == len(L) - 1:
            # Wrap around, we're at the end of the list.
            area += (L[i][0] * L[0][1]) - (L[i][1] * L[0][0])
        else:
            area += (L[i][0] * L[i + 1][1]) - (L[i][1] * L[i + 1][0])

    return abs(area / 2)

def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    assert(almostEqual(areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]), 45.5))
    assert(almostEqual(areaOfPolygon([(9,7), (11,2), (2,2), (4, 10)]), 45.5))
    assert(almostEqual(areaOfPolygon([(0, 0), (0.5,1), (1,0)]), 0.5))
    assert(almostEqual(areaOfPolygon([(0, 10), (0.5,11), (1,10)]), 0.5))
    assert(almostEqual(areaOfPolygon([(-0.5, 10), (0,-11), (0.5,10)]), 10.5))
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testAreaOfPolygon()

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
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()