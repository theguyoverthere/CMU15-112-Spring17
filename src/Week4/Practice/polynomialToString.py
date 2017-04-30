#******************************************************************************#
# Author: Tarique Anwer
# Date:   30/4/2017
# Description: Write the function polynomialToString(p) that takes a polynomial
#              as defined in the previous problems and returns a string
#              representation of that polynomial, with these rules:
#              a) Use "n" as the variable
#              b) Use "^" for exponentation (though that means "bitwise-xor"
#                 in Python)
#              c) Include a space before/after each "+" or "-" sign
#              d) Do not include 0 coefficients (unless the entire polynomial
#                 equals 0)
#              So polynomialToString([2,-3,0,4]) returns "2n^3 - 3n^2 + 4"
#******************************************************************************#
import cs112_s17_linter

def polynomialToString(p):
    """
    Takes a polynomial which is represented by its coefficients in a list and
    returns a string representation of that polynomial, with these rules:
    a) Uses "n" as the variable
    b) Uses "^" for exponentation (though that means "bitwise-xor" in Python)
    c) Includes a space before/after each "+" or "-" sign
    d) Does not include 0 coefficients (unless the entire polynomial equals 0)

    :param p: List of coefficients of a Polynomial.

    :return: The string representation of the Polynomial. Example:
             polynomialToString([2,-3,0,4]) returns "2n^3 - 3n^2 + 4"
    """
    result = ""

    if p == [0] * len(p):
        for i in range(len(p)):
            ri = len(p) - i - 1
            result += str(p[i]) + "n^" + str(ri) + " + "

        return result[: len(result) - 3]

    for i in range(len(p)):
        ri = len(p) - i - 1       #degree of polynomial p

        if p[i] != 0:
            if ri == len(p) - 1:
                sign = ""
            elif p[i] > 0:
                sign = " + "
            else:
                sign = " - "

            degree = "n^" + str(ri) if ri > 0 else ""

            result += sign + str(abs(p[i])) + degree

    return result

def testPolynomialToString():
    print("Testing polynomialToString()...", end="")
    assert(polynomialToString([0,0,0,0]) == "0n^3 + 0n^2 + 0n^1 + 0n^0")
    assert(polynomialToString([2,-3,0,4]) == "2n^3 - 3n^2 + 4")
    assert(polynomialToString([2,0,41,0]) == "2n^3 + 41n^1")
    assert(polynomialToString([7,5,0,41,-1]) == "7n^4 + 5n^3 + 41n^1 - 1")
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testPolynomialToString()

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