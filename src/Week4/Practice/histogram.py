#******************************************************************************#
# Author: Tarique Anwer
# Date:   24/4/2017
# Function: Takes a list of integers between 0 and 100, inclusive, representing
#           exam scores, and returns a string representing a histogram of that
#           data.
# Args:     a: A List of Numbers
# Returns:  A string depicting the data as a histogram.
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def histogram(a):
    frequency = [0] * 10
    result = ""

    for i in range(len(a)):
        if a[i] < 10:
            frequency[0] += 1
        elif a[i] < 20:
            frequency[1] += 1
        elif a[i] < 30:
            frequency[2] += 1
        elif a[i] < 40:
            frequency[3] += 1
        elif a[i] < 50:
            frequency[4] += 1
        elif a[i] < 60:
            frequency[5] += 1
        elif a[i] < 70:
            frequency[6] += 1
        elif a[i] < 80:
            frequency[7] += 1
        elif a[i] < 90:
            frequency[8] += 1
        else:
            frequency[9] += 1

    for i in range(len(frequency) - 1):
        result += str(i) + '0-' + str(i) + '9: ' + ('*' * frequency[i]) + '\n'

    result += '90++ : ' + ('*' * frequency[len(frequency) - 1]) + '\n'

    return result

def testHistogram():
    print("Testing alternatingSum()...", end="")
    assert(histogram([73, 62, 91, 74, 100, 77]) ==
           ("00-09: \n10-19: "       +
            "\n20-29: \n30-39: "     +
            "\n40-49: \n50-59: "     +
            "\n60-69: *\n70-79: ***" +
            "\n80-89: \n90++ : **\n"))
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testHistogram()

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