#################################################
# Hw2
#################################################

import cs112_s17_linter
import math

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
# nthKaprekarNumber(n)
#################################################

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def sumPartition(n, partitionSize):
    lPart = 0
    rPart = 0
    m = n

    for i in range(partitionSize):
        nthDigit = m % 10
        rPart += nthDigit * (10 ** i)
        m //= 10

    if rPart == 0: return -1
    lPart = (n - rPart) // (10 ** partitionSize)
    return lPart + rPart

def isKaprekarNumber(n):
    square    = n ** 2
    numDigits = digitCount(square)

    for i in range(numDigits):
        if sumPartition(square, i + 1) == n: return True

    return False

def nthKaprekarNumber(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if isKaprekarNumber(guess):
            found += 1

    return guess


#################################################
# integral(f, a, b, N)
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return abs(d2 - d1) < epsilon

def integral(f, a, b, N):
    trapezoidHeight = (b - a) / N
    totalArea = 0

    for i in range(N):
        xa = a + (i * trapezoidHeight)
        xb = xa + trapezoidHeight

        totalArea += ((f(xa) + f(xb)) * trapezoidHeight / 2)

    return totalArea

#################################################
# nearestKaprekarNumber(n)
#################################################
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def sumPartition(n, partitionSize):
    lPart = 0
    rPart = 0
    m = n

    for i in range(partitionSize):
        nthDigit = m % 10
        rPart += nthDigit * (10 ** i)
        m //= 10

    if rPart == 0: return -1
    lPart = (n - rPart) // (10 ** partitionSize)
    return lPart + rPart

def isKaprekarNumber(n):
    square    = n ** 2
    numDigits = digitCount(square)

    for i in range(numDigits):
        if sumPartition(square, i + 1) == n: return True

    return False

# Return the strictly left Kaprekar number between
# the loweBound and upperBound. Start searching from
# upperBound and move towards lowerBound

def findLeftKaprekar(lowerBound, upperBound):
    guess = upperBound

    while guess > lowerBound:
        guess -= 1
        if isKaprekarNumber(guess): return guess, (upperBound - guess)

    return -1, -1  # Invalid Kaprekar

def findRightKaprekar(lowerBound, upperBound):
    guess = lowerBound

    if upperBound == 0:
        while True:
            guess += 1
            if isKaprekarNumber(guess): break
    else:
        while guess < upperBound:
            guess += 1
            if isKaprekarNumber(guess): break

    return guess, (guess - lowerBound)

def nearestKaprekarNumber(n):
    m = math.floor(n)
    if n < 0: return 1
    elif isKaprekarNumber(m): return m

    leftKaprekar,  distanceLeft  = findLeftKaprekar(0, m)
    if distanceLeft != -1 :
        upperBound = roundHalfUp(n) + distanceLeft + 1
        rightKaprekar, distanceRight = findRightKaprekar(m, upperBound + 1)
    else:
        rightKaprekar, distanceRight = findRightKaprekar(m, 0)

    distanceLeft  += abs(n - m)
    distanceRight -= abs(n - m)

    if distanceLeft == -1:
        return rightKaprekar
    if distanceLeft == distanceRight:
        return min(leftKaprekar, rightKaprekar)
    elif distanceLeft < distanceRight:
        return leftKaprekar
    else: return rightKaprekar


#################################################
# carrylessMultiply(x, y)
#################################################

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def carrylessAdd(x, y):
    nxDigits = digitCount(x)
    nyDigits = digitCount(y)
    carryLessSum = 0

    for i in range(max(nxDigits, nyDigits)):
        nthDigitX = x % 10
        nthDigitY = y % 10

        nthDigitS = nthDigitX + nthDigitY
        if nthDigitS >= 10: nthDigitS %= 10

        carryLessSum += nthDigitS * (10 ** i)
        x //= 10
        y //= 10

    return carryLessSum

# 643 x
#  59 y
# ---
# 467  (643 * 9)                ==  Multiple Carryless Sum
# Normal Multiplication in the line below
# 005   carryless add (643 * 50) == (Multiple Carryless Sum * 10)
# ----- Carryless Sum
#  417
#

def carrylessMultiply(x, y):
    previousRunningSum = 0
    numDigits = digitCount(y)

    for i in range(numDigits):
        nthDigits = y % 10
        rowSum    = 0

        for j in range(nthDigits):
            carryLessSum = carrylessAdd(rowSum, x)
            rowSum = carryLessSum

        rowSum *= (10 ** i)

        runningSum = carrylessAdd(rowSum, previousRunningSum)
        previousRunningSum = runningSum
        y //= 10

    return runningSum


#################################################
# nthSmithNumber(n)
#################################################

def isPrime(n):
    if n == 2:
        return True
    elif (n < 2) or (n % 2 == 0):
        return False

    for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
        if n % factor == 0:
            return False
    return True

def isPrimeFactor(m, n):
    return isPrime(n) and m % n == 0

def digitSum(n):
    sumOfDigits = 0

    while n > 0:
        nthDigit = n % 10
        sumOfDigits += nthDigit
        n //= 10

    return sumOfDigits

def isSmithNumber(n):
    if isPrime(n) : return False
    factorDigitSum = 0
    m = n

    for factor in range(2, math.floor(n / 2) + 1):
        if m == 1: break

        if isPrimeFactor(n, factor):
            highestPower = 0

            while True:
                if m == 1 or m % factor != 0: break
                highestPower += 1
                m //= factor

            factorDigitSum += highestPower * digitSum(factor)

    return factorDigitSum == digitSum(n)

def nthSmithNumber(n):
    found = 0
    guess = 0

    while found <= n:
        guess += 1
        if isSmithNumber(guess):
            found += 1

    return guess

##### Bonus #####

#################################################
# play112(game)
#################################################
# digitCount(n) takes a possibly-negative int value n
# and returns the number of digits in n

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count

def kthDigit(n, k):
    #Break the number into two parts using (abs(n) % (10 ** (k + 1)))
    #Get the first digit of the resultant number using (10 ** k)
    return (abs(n) % (10 ** (k + 1))) // (10 ** k)

# getLeftmostDigit(n) takes a non-negative int n and returns
# the leftmost digit (that is, the one with the highest place value).

def getLeftmostDigit(n):
    numDigits = digitCount(n)
    return kthDigit(n, numDigits - 1)

# replaceKthDigit(n, k, d) takes a non-negative int n, a non-negative int k,
# and an int d where 0<=d<=9, and returns the number resulting by replacing
# the kth digit (where k is defined as in kthDigit, above) of the number n
# with the digit d.

def replaceKthDigit(n, k, d):

    # As an example, replace 6 in the number below, with 5.
    # n = 12345 |6| 78901
    #Break the number into two parts using (abs(n) % (10 ** (k + 1))
    # remainder = 678901
    # n - remainder = 12345 000000
    # Divide 678901 into two parts as 6 | 78901
    # remainder2 = 78901
    # New Number = 12345 000000 + 78901 + (5 * 100000)

    # remainder = (abs(n) % (10 ** (k + 1)))
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))=
    # (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    remainder = (abs(n) % (10 ** (k + 1)))
    result    = (abs(n) - remainder) + (d * (10 ** k)) + (remainder % (10 ** k))

    if n < 0 : result *= -1
    return result

# clearLeftmostDigit(n) takes a non-negative int n and returns the
# number resulting by deleting the leftmost digit.

def clearLeftmostDigit(n):
    numDigit = digitCount(n)
    return replaceKthDigit(n, numDigit - 1, 0)

# isFull(board) takes a board as specified above and returns True
# if that board is full (no empty spaces), and False otherwise.

def isFull(board):
    while board > 0:
        if board % 10 == 8:
            return False

        board //= 10
    return True


#  isWin(board) takes a board as specified above and returns
#  True if that board is a win (contains 112), and False otherwise.

def isWin(board):
    # Loop while the board size is greater than 2
    while board > 99:
        if (kthDigit(board, 0) == 2 and
            kthDigit(board, 1) == 1 and
            kthDigit(board, 2) == 1):

            return True

        board //= 10

    return False

# Takes a positive integer number of moves, and returns
# an empty board(all 8's) for a game with that many moves.

def makeBoard(moves):
    board = 0

    for i in range(moves):
        board += 8 * (10 ** i)

    return board

# makeMove takes a board as specified above, an int position on the board
# (where 1 is the leftmost position), and an int move (1 or 2), and returns
# the new board that results by making the given move in the given position.
#
# If the move is illegal, however, the function instead returns a specific
# error message indicating the nature of the problem.
#
# In particular, if the move is not a 1 or a 2, returns "move must be 1 or 2!".
# If the position is not on the board, returns "offboard!".
# If the position is not empty, return "occupied!".

def makeMove(board, position, move):
    boardSize = digitCount(board)

    if not (move == 1 or move == 2):
        return "move must be 1 or 2!"
    elif position > boardSize:
        return "offboard!"
    elif not kthDigit(board, boardSize - position) == 8:
        return "occupied!"
    else:
        return replaceKthDigit(board, boardSize - position, move)

def play112(game):
    playerTurn = 0
    boardSize  = getLeftmostDigit(game)
    game       = clearLeftmostDigit(game)
    board      = makeBoard(boardSize)

    if game == 0:
        return "88888: Unfinished!"

    while game > 0:
        #Alternate between two players
        playerTurn += 1

        if playerTurn == 3:
            playerTurn = 1

        #Get next move to be made
        position = getLeftmostDigit(game)
        game     = clearLeftmostDigit(game)
        move     = getLeftmostDigit(game)

        #If the board is not already full, make the move
        if isFull(board):
            break
        else:
            prevBoard = board
            board     = makeMove(prevBoard, position, move)

            if isinstance(board, int): #Successful move
                if isWin(board):
                    return str(board) + ": Player " + str(playerTurn) + " wins!"
            else: #Unsuccessful move
                return str(prevBoard) + \
                       ":" + " Player " + str(playerTurn) + ": " + board

        game = clearLeftmostDigit(game)

    if isWin(board):
        return str(board) + ": Player " + str(playerTurn) + " wins!"
    else:
        if isFull(board):
            return str(board) + ": Tie!"
        else:
            return str(board) + ": Unfinished!"
######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    #kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    #bigKaps = [994708, 999999]
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    # assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testNthKaprekarNumber()
    testIntegral()
    testNearestKaprekarNumber()
    testCarrylessMultiply()
    testNthSmithNumber()
    testBonusPlay112()

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
        #'range,reversed,str,' # added 'str' for play112 bonus
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
