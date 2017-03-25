import cs112_s17_linter

def hasEmbeddedQuote(line, quoteFound):

    posDoubleQuote = line.find("\"\"\"")
    posSingleQuote = line.find("\'\'\'")
    posComment     = line.find("#")

    if posComment != -1:
        if line.find("\'#\'") == posComment - 1:
            posComment = -1
        elif line.find("\"#\"") == posComment - 1:
            posComment = -1
        elif line.find("\'\'\'#\'\'\'") == posComment - 1:
            posComment = -1
        elif quoteFound:
            posComment = -1

    if posDoubleQuote == -1 and posSingleQuote == -1:
        return False
    elif posComment == -1:
        return True
    elif (posDoubleQuote != -1) and (posDoubleQuote < posComment):
        return True
    elif (posSingleQuote != -1) and (posSingleQuote < posComment):
        return True
    else:
        return False

def extractFunctionName(line):

    function = ""

    if line.find(")") > line.find("<"):
        start = line.find(" ") + 1
        end   = line.find("(")

        function = line[start : end]

    return function

def topLevelFunctionNames(code):
    result = ""
    quoteFound = False

    for line in code.splitlines():
        if quoteFound:
            if hasEmbeddedQuote(line, quoteFound):
                quoteFound = False
            continue

        if line.startswith("def "):
            topLevelFunction = extractFunctionName(line)

            if not topLevelFunction ==  "":
                if result.find(topLevelFunction) == -1:
                    if result == "":
                        result += topLevelFunction
                    else:
                        result += "." + topLevelFunction

            #Look for triple quotes
            if hasEmbeddedQuote(line, quoteFound):
                quoteFound = True

    return result

def testBonusTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testBonusTopLevelFunctionNames()

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
