#******************************************************************************#
# Author: Tarique Anwer
# Date:   30/4/2017
# Description: We can represent a polynomial as a list of its
#           coefficients. For example, [2, 3, 0, 4] could represent the
#           polynomial 2x**3 + 3x**2 + 4. With this in mind, write the function
#           evalPolynomial(coeffs, x) that takes a list of coefficients and a
#           value x and returns the value of that polynomial evaluated at that x
#           value. For example, evalPolynomial([2,3,0,4], 4) returns 180
#           (2*4**3 + 3*4**2 + 4 = 2*64 + 3*16 + 4 = 128 + 48 + 4 = 180).
#******************************************************************************#
import cs112_s17_linter

def evalPolynomial(coeffs, x):
    """
    Takes a list of coefficients representing a polynomial and and a value x and
    returns the value of the polynomial evaluated at that x.

    :param coeffs: List of coefficients of the polynomial. For example, the
     polynomial 2x**3 + 3x**2 + 4 can be represented as [2, 3, 0, 4]

    :param x: The value at which the polynomial needs to be evaluated.

    :return:  Value of the polynomial evaluated at the given "x" and returned as
     an integer.

    """
    result = 0

    for i in range(len(coeffs)):
        result += coeffs[i] * (x ** (len(coeffs) - i - 1))

    return result

def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    assert(evalPolynomial([2,3,0,4], 4) == 180)
    assert(evalPolynomial([1,1,0,0], 2) == 12)
    assert(evalPolynomial([4,1,0,-19], 8) == 2093)
    assert(evalPolynomial([-3,0,0,1,0,7], 3) == -713)
    assert(evalPolynomial([0,0,0,0,0,0], 8) == 0)
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