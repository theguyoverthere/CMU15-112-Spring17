#******************************************************************************#
# Author: Tarique Anwer
# Date:   22/4/2017
# Function: Takes a possibly-unsorted list of words (all lowercase) and returns
#           the first word alphabetically in the list that contains the most
#           anagrams of itself in the list. If there are ties, it still returns
#           just the first word alphabetically.
# Args:     List of strings(all lowercase)
# Returns:  String with the maximum number of anagrams(Permutations really)
# Raises:   NA
#******************************************************************************#
import math
import cs112_s17_linter

def hashString(s):
    hashedString = ""

    for i in range(len(s)):
        if s[i] not in hashedString:
            hashedString += s[i]

    return hashedString

def countAnagrams(s):
    denominator = 1
    hashedString = hashString(s)
    frequency = [0] * len(hashedString)

    for i in range(len(s)):
        frequency[hashedString.index(s[i])] += 1

    for i in range(len(hashedString)):
        if frequency[i] > 1:
            denominator *= math.factorial(frequency[i])

    return int(math.factorial(len(s)) / denominator)

def mostAnagrams(a):
    if len(a) == 0: return ""

    maxAnagrams = 0
    position    = 0

    for index in range(len(a)):
        count = countAnagrams(a[index])
        if count > maxAnagrams:
            maxAnagrams = count
            position = index

    return a[position]


def testMostAnagrams():
    print("Testing alternatingSum()...", end="")
    assert(mostAnagrams([]) == "")
    assert(mostAnagrams(["abc"]) == "abc")
    assert(mostAnagrams(["abc", "def"]) == "abc")
    assert(mostAnagrams(["abc", "def", "aaaaaaaaaaaaaaa"]) == "abc")
    assert(mostAnagrams(["aaaaa", "bb", "c"]) == "aaaaa")
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testMostAnagrams()

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

