#******************************************************************************#
# Author: Tarique Anwer
# Date:   30/4/2017
# Description: Write the function multiplyPolynomials(p1, p2) which takes two
#              polynomials as defined in the previous problem and returns a
#              third polynomial which is the product of the two. For example,
#              multiplyPolynomials([2,0,3], [4,5]) represents the problem
#              (2x**2 + 3)(4x + 5), and: (2x**22 + 3)(4x + 5) =
#              8x**3 + 10x**2 + 12x + 15 And so this returns [8, 10, 12, 15].
#******************************************************************************#
import cs112_s17_linter

def multiplyPolynomials(p1, p2):
    """
    Takes two lists of Polynomial coefficients, each representing a polynomial
    and returns a list representing the coefficients of the polynomial
    obtained as a result of the multiplication of the two.

    :param p1: Coefficients of the first polynomial represented as a list.
    :param p2: Coefficients of the second polynomial represented as a list.

    :return: Coefficients of the resultant polynomial, again represented as a
            list.
    """
    result = [0] * (len(p1) + len(p2) - 1)

    for i in range(len(p1)):
        ri = len(p1) - i - 1       #degree of polynomial p1
        for j in range(len(p2)):
            rj = len(p2) - j - 1   #degree of polynomial p2

            result[len(result) -(ri + rj) - 1] += p1[i] * p2[j]

    return result

def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    assert(multiplyPolynomials([3], [4, -5]) == [12, -15])
    assert(multiplyPolynomials([2, 0, 3], [4, 5]) == [8, 10, 12, 15])
    assert(multiplyPolynomials([4, -5], [2, 3, -6]) == [8, 2, -39, 30])
    assert(multiplyPolynomials([3, 2], [4, -7, 5]) == [12, -13, 1, 10])
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testEvalPolynomial()

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