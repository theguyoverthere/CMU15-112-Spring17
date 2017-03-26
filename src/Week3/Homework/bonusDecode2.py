import cs112_s17_linter
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


def testBonusDecode2():
    testBonusDecode("testBonusDecode2", bonusEncode2, bonusDecode2)

#################################################
# testAll and main
#################################################

def testAll():
    testBonusDecode2()

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

