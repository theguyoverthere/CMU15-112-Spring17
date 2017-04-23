import cs112_s17_linter
#******************************************************************************#
# Author: Tarique Anwer
# Date:   9/4/2017
# Function: Takes a list a and returns True if a == b*k for some list b and some
#           value k>1, and False otherwise. For example,
#           repeatingPattern([1,2,3,1,2,3]) returns True (b==[1,2,3] and k=2).
# Args:     A List of Numbers
# Returns:  Boolean indicating whether a repeating pattern exists in the list.
# Raises:   NA
#******************************************************************************#
def repeatingPattern(a):
    count = a.count(a[0])

    if len(a) % count == 0:
        lo = 0
        hi = int(len(a) / count)
        step = hi

        for index in range(count - 1):
            if a[lo: hi] != a[hi: hi + step]:
                return False
            lo += step
            hi += step

        return True

    return False


def testrepeatingPattern():
    print("Testing repeatingPattern()...", end="")
    assert(repeatingPattern([1,1]) == True)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testrepeatingPattern()

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
