import cs112_s17_linter

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

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\n\n\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") ==
                              "a b c ")
    print("Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    testCollapseWhitespace()

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

