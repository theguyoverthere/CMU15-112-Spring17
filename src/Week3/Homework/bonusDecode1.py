import cs112_s17_linter
import random
import string

def bonusEncode1(msg):
	result = ""

	for c in msg:
		if (c.islower()):
			c = chr(ord('a') + (ord(c) - ord('a') + 1) % 26)
		result += c

	return result

def bonusDecode1(msg):
	result = ""

	for c in msg:
		if c.islower():
			c = chr(ord('a') + (ord(c) - ord('a') - 1) % 26)
		result += c

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

def testBonusDecode1():
    testBonusDecode("testBonusDecode1", bonusEncode1, bonusDecode1)

#################################################
# testAll and main
#################################################

def testAll():
    testBonusDecode1()

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
