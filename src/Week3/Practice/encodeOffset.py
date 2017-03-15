import cs112_s17_linter

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

#################################################
# testAll and main
#################################################

def testAll():
    testEncodeOffset()

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

