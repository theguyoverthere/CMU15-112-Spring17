#################################################
# Week3 Practice
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
# Tue Lecture
#################################################

#################################################
# vowelCount(s)
#################################################
def vowelCount(s):
    count = 0

    for c in s:
        if c.lower() in "aeiou":
            count += 1

    return count

#################################################
# interleave(s1, s2)
#################################################
def interleave(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    result = ""

    for i in range(max(len1, len2)):
        if i < len1 :result += s1[i]
        if i < len2 :result += s2[i]

    return result

#################################################
# hasBalancedParentheses(s)
#################################################
def hasBalancedParentheses(s):
    leftParenCount = 0
    rightParenCount = 0

    lSum = 0
    rSum = 0

    for i in range(len(s)):
        if s[i] == "(":
            leftParenCount += 1
            lSum += i
        elif s[i] == ")":
            rightParenCount += 1
            rSum += i

    return (leftParenCount == rightParenCount) and (lSum <= rSum)

#################################################
# Wed Recitation
#################################################

#################################################
# rotateStringLeft(s, k)
#################################################
def rotateStringLeft(s, k):
    k %= len(s)

    leftSplit = s[:k]
    rightSplit = s[k:]

    return rightSplit + leftSplit

#################################################
# rotateStringRight(s, k)
#################################################
def rotateStringRight(s, k):
    k %= len(s)

    leftSplit = s[:-k]
    rightSplit = s[-k:]

    return rightSplit + leftSplit

################################################
# wordWrap(text, width)
################################################
def wordWrap(text, width):
    result = ""
    resultWithNoSpaces = ""
    charCount = 0

    for c in text:
        charCount += 1
        result += c

        if charCount % 4 == 0 :
            result += '\n'

    for line in result.splitlines():
        resultWithNoSpaces += line.strip().replace(" ", "*") + '\n'

    return resultWithNoSpaces[:-1]

################################################
# largestNumber(n)
################################################
def largestNumber(n):
    largestNum = -1

    for word in n.split():
        if word.isdigit() and int(word) > largestNum:
            largestNum = int(word)

    if largestNum != -1 :
        return largestNum
    else:
        return None


#################################################
# Thu Lecture
#################################################

################################################
# longestSubpalindrome(s)
################################################
def isPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i -1]:
            return False
    return True

#Brute Force it.
def longestSubpalindrome(s):
    if isPalindrome(s):
        return s

    longestPalindrome = ""
    palindromeLength = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i : j]

            if isPalindrome(substring):
                if len(substring) == palindromeLength:
                    if substring > longestPalindrome:
                        longestPalindrome = substring
                elif len(substring) > palindromeLength:
                    longestPalindrome = substring
                    palindromeLength = j - i

    return longestPalindrome

################################################
# leastFrequentLetters(s)
################################################

def minNonZeroDigit(n):
    smallestNonZeroDigit = 9

    while n > 0:
        nthDigit = n % 10

        if (nthDigit != 0) and (nthDigit < smallestNonZeroDigit):
            smallestNonZeroDigit = nthDigit

        n //= 10

    return smallestNonZeroDigit

def leastFrequentLetters(s):
    if s == "" : return ""
    lookupString = ""
    result = ""

    for c in string.ascii_lowercase:
        lookupString += str(s.lower().count(c))

    lowestFrequency = str(minNonZeroDigit(int(lookupString)))

    for i in range(len(lookupString)):
        if lookupString[i] == lowestFrequency:
            result += string.ascii_lowercase[i]

    return result

# some interactive console game!

#################################################
# Extra Practice
#################################################

#################################################
# sameChars(s1, s2)
#################################################
def compareLookupStrings(n1, n2):

    if (n1 == 0 and n2 != 0) or (n1 != 0 and n2 == 0):
        return False

    while n1 > 0 and n2 > 0:
        nthDigit1 = n1 % 10
        nthDigit2 = n2 % 10

        if (nthDigit1 * nthDigit2 == 0) and (nthDigit1 + nthDigit2 > 0):
            return False

        n1 //= 10
        n2 //= 10

    return True

def sameChars(s1, s2):
    if isinstance(s1, str) and isinstance(s2, str):
        if s1 == "" and s2 == "": return True
        else:
            lookupString1 = ""
            lookupString2 = ""

            for c in string.ascii_letters:
                lookupString1 += str(s1.count(c))
                lookupString2 += str(s2.count(c))

            return compareLookupStrings(int(lookupString1), int(lookupString2))

    return False

#################################################
# mostFrequentLetters(s)
#################################################
def maxNonZeroDigit(n):
    largestNonZeroDigit = 0

    while n > 0:
        nthDigit = n % 10

        if (nthDigit != 0) and (nthDigit > largestNonZeroDigit):
            largestNonZeroDigit = nthDigit

        n //= 10

    return largestNonZeroDigit

def mostFrequentLetters(s):
    if s == "" : return ""

    lookupString = ""
    result = ""

    for c in string.ascii_lowercase:
        lookupString += str(s.lower().count(c))

    highestFrequency = str(maxNonZeroDigit(int(lookupString)))

    for i in range(len(lookupString)):
        if lookupString[i] == highestFrequency:
            result += string.ascii_uppercase[i]

    return result

#################################################
# areAnagrams(s1, s2)
#################################################
def areAnagrams(s1, s2):
    lookupString1 = ""
    lookupString2 = ""

    for c in string.ascii_lowercase:
        lookupString1 += str(s1.lower().count(c))
        lookupString2 += str(s2.lower().count(c))

    return lookupString1 == lookupString2

#################################################
# collapseWhitespace(s)
#################################################
def isSpaceCharacter(s):
    return (s == " ") or (s == '\n') or (s == '\t')

def collapseWhitespace(s):
    result = ""
    spaceFound = False

    for i in range(len(s)):
        if isSpaceCharacter(s[i]):
            if not spaceFound:
                # Previous space not found OR
                # a non-space character has been encountered already.
                spaceFound = True
                result += " "
            continue
        else:
            if spaceFound:
                #Previous space was found,
                # but we have a non-space character now
                spaceFound = False
            result += s[i]

    return  result

#################################################
# replace(s1, s2, s3)
#################################################
def replace(s1, s2, s3):
    previousResult = s1

    if s2 == "" :
        result = ""
        for i in range(len(s1)):
            result += s3 + s1[i]

        return result + s3

    while previousResult.find(s2) != -1:
        if previousResult == s2: break

        result = ""
        result += (previousResult[:previousResult.find(s2)] +
                   s3 +
                   previousResult[previousResult.find(s2) + len(s2):])
        previousResult = result

    return previousResult

#################################################
# encodeOffset(s, d)
#################################################
def encodeOffset(s, d):
    d %= 26
    result = ""

    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                # Look for a wraparound.
                if ord(s[i]) + d > ord('z'):               # Positive Wraparound
                    delta = ord(s[i]) + d - ord('z')
                    result += chr(ord('a') + delta - 1)
                elif ord(s[i]) + d < ord('a'):             # Negative Wraparound
                    delta = abs(ord(s[i]) + d - ord('a'))
                    result += chr(ord('z') - delta + 1)
                else:                                      # No Wrapping
                    result += chr(ord(s[i]) + d)

            else:
                # Look for a wraparound.
                if ord(s[i]) + d > ord('Z'):               # Positive Wraparound
                    delta = ord(s[i]) + d - ord('Z')
                    result += chr(ord('A') + delta - 1)
                elif ord(s[i]) + d < ord('A'):             # Negative Wraparound
                    delta = abs(ord(s[i]) + d - ord('A'))
                    result += chr(ord('Z') - delta + 1)
                else:                                      # No Wrapping
                    result += chr(ord(s[i]) + d)
        else:
            result += s[i]

    return result

#################################################
# decodeOffset(s, d)
#################################################
def encodeOffset(s, d):
    d %= 26
    result = ""

    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                # Look for a wraparound.
                if ord(s[i]) + d > ord('z'):               # Positive Wraparound
                    delta = ord(s[i]) + d - ord('z')
                    result += chr(ord('a') + delta - 1)
                elif ord(s[i]) + d < ord('a'):             # Negative Wraparound
                    delta = abs(ord(s[i]) + d - ord('a'))
                    result += chr(ord('z') - delta + 1)
                else:                                      # No Wrapping
                    result += chr(ord(s[i]) + d)

            else:
                # Look for a wraparound.
                if ord(s[i]) + d > ord('Z'):               # Positive Wraparound
                    delta = ord(s[i]) + d - ord('Z')
                    result += chr(ord('A') + delta - 1)
                elif ord(s[i]) + d < ord('A'):             # Negative Wraparound
                    delta = abs(ord(s[i]) + d - ord('A'))
                    result += chr(ord('Z') - delta + 1)
                else:                                      # No Wrapping
                    result += chr(ord(s[i]) + d)
        else:
            result += s[i]

    return result


def decodeOffset(s, d):
    return encodeOffset(s, -d)

#################################################
# encrypt(msg, pwd)
#################################################
def getMessageToEncrypt(msg):
    message = ""

    for i in range(len(msg)):
        if msg[i].isalpha():
            message += msg[i].upper()

    return message

def getShifts(password, length):
    result = password

    if len(password) < length:
        delta =  length - len(password)

        while delta > len(password):
            result += password
            delta -= len(password)

        for i in range(delta):
            result += password[i]

    return result

def encrypt(msg, pwd):
    if pwd.isupper():
        return "password must be all lowercase"

    message = getMessageToEncrypt(msg)
    shiftString = getShifts(pwd, len(message))
    cipherText = ""

    for i in range(len(message)):
        d = ord(shiftString[i]) - ord('a')

        if ord(message[i]) + d > ord('Z'):            # Wraparound
            delta = ord(message[i]) +  d - ord('Z')
            cipherText += chr(ord('A') + delta - 1)
        else:
            cipherText += chr(ord(message[i]) + d)

    return cipherText

#################################################
# decrypt(msg, pwd)
#################################################
def getShifts(password, length):
    result = password

    if len(password) < length:
        delta =  length - len(password)

        while delta > len(password):
            result += password
            delta -= len(password)

        for i in range(delta):
            result += password[i]

    return result

def decrypt(ciphertext, password):

    shiftString = getShifts(password, len(ciphertext))
    message = ""

    for i in range(len(ciphertext)):
        d = ord(shiftString[i]) - ord('a')

        if ord(ciphertext[i]) - d < ord('A'):            # Wraparound
            delta = abs(ord(ciphertext[i]) -  d - ord('A'))
            message += chr(ord('Z') - delta + 1)
        else:
            message += chr(ord(ciphertext[i]) - d)

    return message

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Passed!")

def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert(hasBalancedParentheses("()") == True)
    assert(hasBalancedParentheses("") == True)
    assert(hasBalancedParentheses("())") == False)
    assert(hasBalancedParentheses("()(") == False) 
    assert(hasBalancedParentheses(")(") == False)
    assert(hasBalancedParentheses("(()())") == True)
    assert(hasBalancedParentheses("((()())(()(()())))") == True)
    assert(hasBalancedParentheses("((()())(()((()())))") == False)
    assert(hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")

def testRotateStringLeft():
    print("Testing rotateStringLeft()...", end="")
    assert(rotateStringLeft("abcde", 0) == "abcde")
    assert(rotateStringLeft("abcde", 1) == "bcdea")
    assert(rotateStringLeft("abcde", 2) == "cdeab")
    assert(rotateStringLeft("abcde", 3) == "deabc")
    assert(rotateStringLeft("abcde", 4) == "eabcd")
    assert(rotateStringLeft("abcde", 5) == "abcde")
    assert(rotateStringLeft("abcde", 25) == "abcde")
    assert(rotateStringLeft("abcde", 28) == "deabc")
    print("Passed!")

def testRotateStringRight():
    print("Testing rotateStringRight()...", end="")
    assert(rotateStringRight("abcde", 0) == "abcde")
    assert(rotateStringRight("abcde", 1) == "eabcd")
    assert(rotateStringRight("abcde", 2) == "deabc")
    assert(rotateStringRight("abcde", 3) == "cdeab")
    assert(rotateStringRight("abcde", 4) == "bcdea")
    assert(rotateStringRight("abcde", 5) == "abcde")
    assert(rotateStringRight("abcde", 25) == "abcde")
    assert(rotateStringRight("abcde", 28) == "cdeab")
    print("Passed!")

def testSameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("abcabcabc", "cba") == True)
    assert(sameChars("cba", "abcabcabc") == True)
    assert(sameChars("abcabcabc", "cbad") == False)
    assert(sameChars("abcabcabc", "cBa") == False)
    assert(sameChars(42,"The other parameter is not a string") == False)
    assert(sameChars("","") == True)
    assert(sameChars("","a") == False)
    print("Passed!")

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("Cat") == 'ACT')
    assert(mostFrequentLetters("A cat") == 'A')
    assert(mostFrequentLetters("A cat in the hat") == 'AT')
    assert(mostFrequentLetters("This is a test") == 'ST')
    assert(mostFrequentLetters("This is an I test?") == 'IST')
    assert(mostFrequentLetters("") == "")
    print("Passed!")

def testWordWrap():
    print("Testing wordWrap()...", end="")
    assert(wordWrap("abcdefghij", 4) == """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg", 4) == """\
a*b
c*de
fg""")
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testLeastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    assert(leastFrequentLetters("abc def! GFE'cag!!!") == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".lower()) == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".upper()) == "bd")
    assert(leastFrequentLetters("") == "")
    assert(leastFrequentLetters("\t \n&^#$") == "")
    noq = string.ascii_lowercase.replace('q','')
    assert(leastFrequentLetters(string.ascii_lowercase + noq) == "q")
    print("Passed!")

def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert(areAnagrams("", "") == True)
    assert(areAnagrams("abCdabCd", "abcdabcd") == True)
    assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\n\n\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") ==
                              "a b c ")
    print("Passed!")

def testReplace():
    print("Testing replace()...", end="")
    (s1, s2, s3) = ("abcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abcdeabcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("babababa", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abb", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "", "q")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "ab", "")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    print("Passed!")

def testEncodeOffset():
    print("Testing encodeOffset()...", end="")
    assert(encodeOffset("ACB", 1) == "BDC")
    assert(encodeOffset("ACB", 2) == "CED")
    assert(encodeOffset("XYZ", 1) == "YZA")
    assert(encodeOffset("ABC", -1) == "ZAB")
    assert(encodeOffset("ABC", -27) == "ZAB")
    assert(encodeOffset("Abc", -27) == "Zab")
    assert(encodeOffset("A2b#c", -27) == "Z2a#b")
    print("Passed!")

def testDecodeOffset():
    print("Testing decodeOffset()...", end="")
    assert(decodeOffset("BDC", 1) == "ACB")
    assert(decodeOffset("CED", 2) == "ACB")
    assert(decodeOffset("YZA", 1) == "XYZ")
    assert(decodeOffset("ZAB", -1) == "ABC")
    assert(decodeOffset("ZAB", -27) == "ABC")
    assert(decodeOffset("Zab", -27) == "Abc")
    assert(decodeOffset("Z2a#b", -27) == "A2b#c")
    print("Passed!")

def testEncrypt():
    print("Testing encrypt()...", end="")
    assert(encrypt("Go Team!", "azby") == "GNUCAL")
    assert(encrypt("a1m2a3z4i5n6g !?!?", "yes") == "YQSXMFE")
    assert(encrypt("", "wow") == "")
    assert(encrypt("Wow!", "AZBY") == "password must be all lowercase")
    print("Passed!")

def testDecrypt():
    print("Testing decrypt()...", end="")
    assert(decrypt("GNUCAL", "azby") == "GOTEAM")
    assert(decrypt("YQSXMFE", "yes") == "AMAZING")
    assert(decrypt("", "wow") == "")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testVowelCount()
    testInterleave()
    testHasBalancedParentheses()
    testRotateStringLeft()
    testRotateStringRight()
    testWordWrap()
    testLargestNumber()
    testLongestSubpalindrome()
    testLeastFrequentLetters()
    testSameChars()
    testMostFrequentLetters()
    testAreAnagrams()
    testCollapseWhitespace()
    testReplace()
    testEncodeOffset()
    testDecodeOffset()
    testEncrypt()
    testDecrypt()

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
