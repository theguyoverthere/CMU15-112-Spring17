# Let the total distance travelled be 2d, velocity of the boat be 'v'
# and the velocity of the river current be 'r'
# => Tup = d / (v - r) and Tdown = d / (v + r)
# => Ttotal = Tup + Tdown
# => Ttotal = (d / (v - r)) + (d / v + r))
# => Ttotal = 2dv / (v ** 2 - r ** 2)
# => v = (2d /Ttotal) + sqrt( 4 d **2 / Ttotal ** 2 + 4 r **2))
# => Tupstream = d / (v - r)


import cs112_s17_linter
import math

def boatVelocity(totalTime, upstreamDistance, riverCurrent):

    return (upstreamDistance/ totalTime) + \
           math.sqrt(((upstreamDistance / totalTime) ** 2) + (riverCurrent ** 2))

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):

    upstreamDistance = totalDistance / 2
    relativeVelocity = boatVelocity(totalTime, upstreamDistance, riverCurrent) - riverCurrent

    return upstreamDistance / relativeVelocity

def testRiverCruiseUpstreamTime():
    print('Testing riverCruiseUpstreamTime()... ', end='')
    assert(math.isclose(riverCruiseUpstreamTime(3, 30, 2), 1.7888736053508778))
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testRiverCruiseUpstreamTime()

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
