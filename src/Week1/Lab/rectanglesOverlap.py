# The assumption is that both the rectangles are parallel!!
# https://silentmatt.com/rectangle-intersection/
#    x,y-----------------.    (0,0)---> x+
#    |                   |    |
#    |                   |h   |
#    |                   |    y+
#    |___________________|
#              w
import cs112_s17_linter

def rectanglesOverlap(x1, y1, w1, h1,
                      x2, y2, w2, h2):
    return ((x2 >= (x1 - w2)) and (x2 <= (x1 + w1)) and
            (y2 >= (y1 - h2)) and (y2 <= (y1 + h1)))

def testNearestOdd():
    print('Testing rectanglesOverlap()... ', end='')

    #Completely Overlapping
    assert(rectanglesOverlap(1, 1, 1, 1,
                             1, 1, 1, 1 ) == True)

    #Completely Inside
    assert(rectanglesOverlap(0, 0, 10, 6,
                             2, 2, 2,  2 ) == True)

    assert(rectanglesOverlap(2, 2,  2, 2,
                             0, 0, 10, 6 ) == True)

    #Overlap at the right edge
    assert(rectanglesOverlap(1, 1, 1, 1,
                             2, 0, 4, 2.5) == True)

   #Partial Overlap
    assert(rectanglesOverlap(2, 1, 4, 2,
                             3, 2, 5, 32.5) == True)

   #No Overlap
    assert(rectanglesOverlap(2, 1, 4, 2,
                             3, 5, 8, 4) == False)
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
