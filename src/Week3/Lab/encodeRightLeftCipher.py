import cs112_s17_linter
import math

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

            if k % 2 == 0:
                for j in range (k, len(message) - noFullRows - 1, rows):
                    cipherText += message[j : j + 1]
                cipherText += chr(filler)
            else:
                cipherText += chr(filler)
                for j in range (len(message) - noFullRows - 1, k - 1, -rows):
                    cipherText += message[j : j + 1]

            filler -= 1

    return str(rows) + cipherText

def testEncodeRightLeftCipher():
    print("Testing encodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 4
    # W T A W
    # E A T N
    # A C D z
    # T K A y
    rightLeft = "4"+"WTAWNTAEACDzyAKT"
    cipher = encodeRightLeftCipher(text, rows)
    assert(rightLeft == cipher)
    print("passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testEncodeRightLeftCipher()

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
