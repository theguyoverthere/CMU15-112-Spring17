import cs112_s17_linter

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

def testEncrypt():
    print("Testing encrypt()...", end="")
    assert(encrypt("Go Team!", "azby") == "GNUCAL")
    assert(encrypt("a1m2a3z4i5n6g !?!?", "yes") == "YQSXMFE")
    assert(encrypt("", "wow") == "")
    assert(encrypt("Wow!", "AZBY") == "password must be all lowercase")
    print("Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    testEncrypt()

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


