#******************************************************************************#
# Author: Tarique Anwer
# Date:   7/5/2017
# Description: First, read about look-and-say numbers on Wikipedia. Then, write
#              the function lookAndSay(a) that takes a list of numbers and
#              returns a list of numbers that results from "reading off" the
#              initial list using the look-and-say method, using tuples for each
#              (count, value) pair. For example:
#              lookAndSay([]) == []
#              lookAndSay([1,1,1]) == [(3,1)]
#              lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
#              lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
#******************************************************************************#
import cs112_s17_linter
import copy

def lookAndSay(a):
    if len(a) == 0: return []

    i = 0
    result = []
    currentPair = [1,0]

    while True:
        currentPair[1] = a[i]

        if i == len(a) - 1:
            result.append(tuple(currentPair))
            break
        elif a[i] == a[i + 1]:
            currentPair[0] += 1
        else:
            result.append(tuple(currentPair))
            currentPair[0] = 1
        i += 1

    return result

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,del,is,pass,repr' +
        'as,class,except,finally,global,lambda,nonlocal,raise,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len,'+
        #'ascii,bin,dir,enumerate,format,help,hex,id,iter,'+
        #'list,oct,slice,sorted,tuple,zip,'+
        '__import__,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,' +
        'eval,exec,filter,frozenset,getattr,globals,' +
        'hasattr,hash,issubclass,' +
        'locals,map,memoryview,next,object,open,property,set,' +
        'setattr,staticmethod,super,' +
        'type,vars,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()