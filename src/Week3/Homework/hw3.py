#################################################
# Hw3
#################################################
import cs112_s17_linter
import math, string

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Autograded Exercises
#################################################

#################################################
# patternedMessage(message, pattern)
#################################################
def patternedMessage(message, pattern):
    result = ""
    messageNoSpaces = ""

    for i in range(len(message)):
        if not message[i].isspace():
            messageNoSpaces += message[i]

    j = 0

    for line in pattern.splitlines():
        result += '\n'

        for i in range(len(line)):
            if line[i].isspace():
                result += " "
            else:
                if j < len(messageNoSpaces):
                    result += messageNoSpaces[j: j + 1]
                else:
                    j = 0
                    result += messageNoSpaces[j: j + 1]
                j += 1

    return result

#################################################
# bestStudentAndAvg(gradebook)
#################################################

def bestStudentAndAvg(gradebook):
    name = ""
    bestStudent = ""
    maxAverage = -99999999999999

    for line in gradebook.splitlines():

        if (len(line.strip()) == 0 or
            line.startswith("#")   or
            line.startswith(" ")):
                continue
        else:
            sum = 0
            count = 0

            for word in line.split(","):
                if word.isalpha():
                    name = word
                else:
                    count += 1
                    sum += int(word)

            studentAverage = sum / count

            if studentAverage >= maxAverage:
                maxAverage = studentAverage
                bestStudent = name

    return bestStudent + ":" + str(roundHalfUp(maxAverage))

###### BONUS #######

#################################################
# topLevelFunctionNames(code)
#################################################

def hasEmbeddedQuote(line, quoteFound):

    posDoubleQuote = line.find("\"\"\"")
    posSingleQuote = line.find("\'\'\'")
    posComment     = line.find("#")

    if posComment != -1:
        if line.find("\'#\'") == posComment - 1:
            posComment = -1
        elif line.find("\"#\"") == posComment - 1:
            posComment = -1
        elif line.find("\'\'\'#\'\'\'") == posComment - 1:
            posComment = -1
        elif quoteFound:
            posComment = -1

    if posDoubleQuote == -1 and posSingleQuote == -1:
        return False
    elif posComment == -1:
        return True
    elif (posDoubleQuote != -1) and (posDoubleQuote < posComment):
        return True
    elif (posSingleQuote != -1) and (posSingleQuote < posComment):
        return True
    else:
        return False

def extractFunctionName(line):

    function = ""

    if line.find(")") > line.find("<"):
        start = line.find(" ") + 1
        end   = line.find("(")

        function = line[start : end]

    return function

def topLevelFunctionNames(code):
    result = ""
    quoteFound = False

    for line in code.splitlines():
        if quoteFound:
            if hasEmbeddedQuote(line, quoteFound):
                quoteFound = False
            continue

        if line.startswith("def "):
            topLevelFunction = extractFunctionName(line)

            if not topLevelFunction ==  "":
                if result.find(topLevelFunction) == -1:
                    if result == "":
                        result += topLevelFunction
                    else:
                        result += "." + topLevelFunction

            #Look for triple quotes
            if hasEmbeddedQuote(line, quoteFound):
                quoteFound = True

    return result

#################################################
# getEvalSteps(expression)
#################################################

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

#################################################
# bonusEncode1(msg)
#################################################

def bonusEncode1(msg):
	result = ""

	for c in msg:
		if (c.islower()):
			c = chr(ord('a') + (ord(c) - ord('a') + 1) % 26)
		result += c

	return result

#################################################
# bonusDecode1(msg)
#################################################

def bonusDecode1(msg):
	result = ""

	for c in msg:
		if c.islower():
			c = chr(ord('a') + (ord(c) - ord('a') - 1) % 26)
		result += c

	return result


#################################################
# bonusEncode2(msg)
#################################################

import string
import random

#0    5    10   15   20    25   30   35    40   45   50   55   60   65   70   75
#+----+----+----+----+-- --+----+----+--- -+----+----+----+----+----+----+----+
#ddd 7jhnkvd1c00N(5aX):\n    0MZ0QX = ""\n    I = HHEuyq.izinm_nftscoo + kkh7b3

# To encode: Fetch the position of each character in msg, and subtract that
# value from the character itself. Wrap around if required.

def bonusEncode2(msg):
    result = ""
    p = string.ascii_letters + string.digits
    for i in range(len(msg)):
        c = msg[i]
        if (c in p): c = p[(p.find(c) - i) % len(p)]
        result += c
    return result

#################################################
# bonusDecode2(msg)
#################################################

def bonusDecode2(msg):
    reference = string.ascii_letters + string.digits
    referenceLength = len(reference)
    result = ""

    for i in range(len(msg)):
        if msg[i].isalnum():
            result += reference[(reference.find(msg[i]) + i) % referenceLength]
        else:
            result += msg[i]

    return result

def bonusEncode3(msg): return 42
def bonusDecode3(msg): return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# playPig (be sure this is below the # ignore_rest line!
#################################################

import random

def playNextRound(playerScore):
    WINNING_SCORE = 100

    option = input("Roll dice (y/n)?").lower()
    while not (option == 'y' or option == 'n'):
                option = input("Please enter a valid option (y/n)?").lower()

    currentScore = playerScore

    while option == "y":
        diceRoll = random.randint(1, 6)

        if diceRoll == 1:
            print("You rolled 1!")
            break

        currentScore += diceRoll

        if currentScore >= WINNING_SCORE:
            print("Current Score: ", currentScore, end="\n")
            print("Congratulations, you've won!")
            return -1
        else:
            print("Current Score: ", currentScore, end="\n")
            option = input("Roll again (y/n)?").lower()

            while not (option == 'y' or option == 'n'):
                option = input("Please enter a valid option (y/n)?").lower()

    return currentScore

def playPig():
    scoreA = 0
    scoreB = 0
    currentPlayer = "Player A"

    while True:
        print("\n" + currentPlayer)

        if currentPlayer == "Player A":
            scoreA = playNextRound(scoreA)
            currentScore = scoreA
        else:
            scoreB = playNextRound(scoreB)
            currentScore = scoreB

        if currentScore == -1 :
            break
        elif currentPlayer == "Player A":
            currentPlayer = "Player B"
        else:
            currentPlayer = "Player A"

    return 0

#################################################
# Test Functions
#################################################

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        msg,pattern = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        observed = patternedMessage(msg, pattern).strip("\n")
        # print("\n\n***********************\n\n")
        # print(msg, pattern)
        # print("<"+patternedMessage(msg, pattern)+">")
        # print("<"+soln+">")
        assert(observed == soln)
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")

def testBonusTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

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

import random

def testBonusDecode(testFn, encodeFn, decodeFn):
    print("Testing " + testFn + "...", end="")
    s1 = ""
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(" \n\n") + random.choice(string.digits)
    for s in ["a", "abc", s1]:
        assert(decodeFn(encodeFn(s)) == s)
    print("Passed!")

def testBonusDecode1():
    testBonusDecode("testBonusDecode1", bonusEncode1, bonusDecode1)

def testBonusDecode2():
    testBonusDecode("testBonusDecode2", bonusEncode2, bonusDecode2)

def testBonusDecode3():
    testBonusDecode("testBonusDecode3", bonusEncode3, bonusDecode3)

#################################################
# testAll and main
#################################################

def testAll():
    testPatternedMessage()
    testBestStudentAndAvg()
    testBonusTopLevelFunctionNames()
    testBonusGetEvalSteps()
    testBonusDecode1()
    testBonusDecode2()
    # testBonusDecode3()

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
