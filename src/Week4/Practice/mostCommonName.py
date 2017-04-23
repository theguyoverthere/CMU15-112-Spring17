#******************************************************************************#
# Author: Tarique Anwer
# Date:   23/4/2017
# Function: Takes a list of names (such as ['Jane', 'Aaron', 'Cindy', 'Aaron'],
#           and returns the most common name in this list (in this case,
#           'Aaron'). If there is more than one such name, return a list of the
#           most common names, in alphabetical order (actually, in whatever
#           order sorted() uses). So mostCommonName(['Jane', 'Aaron', 'Jane',
#          'Cindy', 'Aaron']) returns the list ['Aaron', 'Jane']. If the list is
#           empty, return None. Also, treat names case sensitively, so 'jane'
#           and 'Jane' are different names.
# Args:     a: A list of strings.
# Returns:  A list of strings or None
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def hashList(a):
    hashedList = []
    for i in range(len(a)):
        if a[i] not in hashedList:
            hashedList.append(a[i])

    return hashedList

def mostCommonName(a):
    if len(a) == 0: return None

    result = []
    noDuplicateList = hashList(a)
    frequency = [0] * len(noDuplicateList)

    for i in range(len(a)):
        frequency[noDuplicateList.index(a[i])] += 1

    maxFrequency = max(frequency)

    for i in range(len(noDuplicateList)):
        if frequency[i] == maxFrequency:
            result.append(noDuplicateList[i])

    return sorted(result)

def testMostCommonName():
    print("Testing alternatingSum()...", end="")
    assert(mostCommonName([]) == None)
    assert(mostCommonName(['Jane', 'Aaron', 'Jane', 'Cindy', 'Aaron']) ==
                          ['Aaron', 'Jane'])
    assert(mostCommonName(['Jane', 'Aaron', 'Cindy', 'Aaron']) == ['Aaron'])
    assert(mostCommonName(['Jane', 'jane', 'Cindy', 'Aaron']) ==
                          ['Aaron', 'Cindy', 'Jane', 'jane'])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testMostCommonName()

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
        'setattr,slice,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()