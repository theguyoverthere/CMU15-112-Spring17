import cs112_s17_linter

def binaryOperatorPresent(expression):
    if expression.find("+") != -1:
        return True
    elif expression.find("-")  != -1:
        return True
    elif expression.find("*")  != -1:
        return True
    elif expression.find("/")  != -1:
        return True
    elif expression.find("%")  != -1:
        return True
    elif expression.find("//") != -1:
        return True
    elif expression.find("**") != -1:
        return True

    return False

def nextOperator(expression):
    if expression.find("**") != -1:
        return "**"
    elif expression.find("*")  != -1:
        return "*"
    elif expression.find("%")  != -1:
        return "%"
    elif expression.find("//") != -1:
        return "//"
    elif expression.find("/")  != -1:
        return "/"
    elif expression.find("+")  != -1:
        return "+"
    elif expression.find("-")  != -1:
        return "-"
    return 0

def getLeftOperand(expression, index):

    for i in range(index, 0, -1):

        if (expression[i - 1: i] == "*"  or
            expression[i - 1: i] == "/"  or
            expression[i - 1: i] == "//" or
            expression[i - 1: i] == "%"  or
            expression[i - 1: i] == "+"  or
            expression[i - 1: i] == "-"):

            return int(expression[i: index + 1].strip()), i

    return int(expression[0 : index + 1]), 0

def getRightOperand(expression, index):

    for i in range(index, len(expression)):

        if (expression[i : i + 1] == "*"  or
            expression[i : i + 1] == "/"  or
            expression[i : i + 1] == "//" or
            expression[i : i + 1] == "%"  or
            expression[i : i + 1] == "+"  or
            expression[i : i + 1] == "-"):

            return (int(expression[index : i].strip()), index,
                    len(expression[index : i].strip()))

    return int(expression[index :]), index, len(expression[index :])

def applyOperator(expression, operator):
    index = expression.find(operator)

    leftOperand, leftIndex = getLeftOperand(expression, index - 1)

    if operator == "**" or operator == "//":
        rightOperand, rightIndex, size = getRightOperand(expression, index + 2)
    else:
        rightOperand, rightIndex, size = getRightOperand(expression, index + 1)

    if operator == "**":
        operationResult = leftOperand ** rightOperand
    elif operator == "*":
        operationResult = leftOperand * rightOperand
    elif operator == "/":
        operationResult = leftOperand / rightOperand
    elif operator == "//":
        operationResult = leftOperand // rightOperand
    elif operator == "%":
        operationResult = leftOperand % rightOperand
    elif operator == "+":
        operationResult = leftOperand + rightOperand
    elif operator == "-":
        operationResult = leftOperand - rightOperand

    return (expression[: leftIndex] +
            str(operationResult)       +
            expression[rightIndex + size :])

def getPrefix(expression):
    prefix = ""

    for i in range(len(expression)):
        prefix += " "

    return prefix

def getEvalSteps(expression):
    prefix = getPrefix(expression)
    reducedExpression = expression
    result = ""

    while binaryOperatorPresent(reducedExpression):
        operator = nextOperator(reducedExpression)
        reducedExpression = applyOperator(reducedExpression, operator)
        if result == "":
            result += expression + " = " + reducedExpression + "\n"
        else:
            result += prefix + " = " + reducedExpression + "\n"

    if result == "":
        return expression + " = " + expression
    else:
        return result[: len(result) - 1]

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    testBonusGetEvalSteps()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,repr' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
