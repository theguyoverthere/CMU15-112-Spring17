import cs112_s17_linter
import math

def reverseString(s):
    return s[::-1]

def decodeRightLeftCipher(encodedMessage):
    rows = int (encodedMessage[:1])
    encodedMessage = encodedMessage[1:]
    column = int (len(encodedMessage) / rows)
    cipherText = ""
    originalText = ""

    # Reverse alternate blocks of characters so that they
    # all read left to right.
    for i in range(0, len(encodedMessage), column):
        if (i / column) % 2 == 1:
            cipherText += reverseString(encodedMessage[i: i + column])
        else:
            cipherText += encodedMessage[i: i + column]

    for i in range(column):
        for j in range(i, len(cipherText), column):
            if cipherText[j: j + 1].isupper():
                originalText += cipherText[j: j + 1]

    return originalText


def encodeRightLeftCipher(message, rows):
    cipherText = ""
    rowCount = 0
    columns = math.ceil(len(message) / rows)
    noFullRows = len(message) % rows
    if noFullRows == 0: noFullRows = rows

    for i in range(noFullRows):
        rowCount += 1

        if i % 2 == 0:
            for j in range (i, (rows * columns) + 1, rows):
                cipherText += message[j : j + 1]
        else:
            for j in range (rows * (columns - 1) + i, i - 1, -rows):
                cipherText += message[j : j + 1]

    if noFullRows < rows:
        filler = ord('z')

        for k in range(rowCount, rowCount + rows - noFullRows):

            rowsBelow = rows - k - 1

            if k % 2 == 0:
                for j in range (k, len(message) - noFullRows - 1, rows):
                    cipherText += message[j : j + 1]
                cipherText += chr(filler)
            else:
                cipherText += chr(filler)
                for j in range (((rows * columns) - 1) - rows - rowsBelow,
                                 k - 1, -rows):
                    cipherText += message[j : j + 1]

            filler -= 1

    return str(rows) + cipherText

def testDecodeRightLeftCipher():
    print("testing decodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 6
    cipher = encodeRightLeftCipher(text, rows)
    plaintext = decodeRightLeftCipher(cipher)
    assert(plaintext == text)
    print("passed!")


#################################################
# testAll and main
#################################################

def testAll():
    testDecodeRightLeftCipher()

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

