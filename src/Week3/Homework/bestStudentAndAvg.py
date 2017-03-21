import cs112_s17_linter
import decimal

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def bestStudentAndAvg(gradebook):
    name = ""
    bestStudent = ""
    maxAverage = -99999999999999

    for line in gradebook.splitlines():

        if len(line.strip()) != 0:
            if line.startswith("#") or line.startswith(" "):
                continue
            else:
                sum = 0
                count = 0

                for word in line.split(","):
                    if word.isalpha():
                        name = word
                    else:
                        count += 1
                        sum += int(word)

                lineAverage = sum / count

                if lineAverage >= maxAverage:
                    maxAverage = lineAverage
                    bestStudent = name

    return bestStudent + ":" + str(roundHalfUp(maxAverage))

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testBestStudentAndAvg()

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
