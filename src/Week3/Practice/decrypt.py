import cs112_s17_linter

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

