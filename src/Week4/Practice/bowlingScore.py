#******************************************************************************#
# Author: Tarique Anwer
# Date:   29/4/2017
# Description: Background: in bowling, a bowler gets 2 throws per frame for 10
#              frames, where each frame begins with 10 pins freshly positioned,
#              and the score is the sum of all the pins knocked down. However,
#              if the bowler knocks down all 10 pins on the first throw of a
#              frame, it is called a "strike", and they do not get a second
#              throw in that frame; also, the number of pins knocked down in the
#              next two throws are added to the score of that frame. Also, if
#              the bowler knocks down the rest of the 10 pins on the second
#              throw in a frame, that is called a "spare", and the number of
#              pins knocked down in the next throw are added to the score of
#              that frame. Finally, if there is a spare or strike in the final
#              frame, then the bowler gets one extra throw in that frame (but if
#              there is a subsequent strike, they still get only that one extra
#              throw). With all this in mind, write the function bowlingScore
#              that takes a list of the number of pins knocked down on each
#              throw and returns the score. Note that throws skipped due to
#              strikes are not listed, so the best possible result is a list of
#              12 10's (all strikes), which would score 300 points.
# Args:     pinsPerThrowList: List
# Returns:  Integer
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def updateStrikes(pinsPerThrowList):
    updatedList = []
    currentFrame = []
    frames = 0

    for i in range(len(pinsPerThrowList)):
        currentFrame.append(pinsPerThrowList[i])

        if pinsPerThrowList[i] == 10:
            currentFrame.append(0)

        if len(currentFrame) == 2:
            frames += 1
            updatedList.append(currentFrame)
            currentFrame = []

        if frames == 9: break

    updatedList.append(pinsPerThrowList[i + 1:])

    if len(updatedList[len(updatedList) - 1]) == 1:
        updatedList[len(updatedList) - 1].append(0)

    return updatedList

def bowlingScore(pinsPerThrowList):
    score  = 0
    frameList = updateStrikes(pinsPerThrowList)
    frameScore = [0] * len(frameList)

    for i in range(len(frameList)):

        if (i != 0) and (frameList[i - 1])[0] == 10:
            if i < len(frameList) - 1 and (frameList[i])[0] == 10:
                frameScore[i - 1] += ((frameList[i])[0] + (frameList[i + 1])[0])
            else:
                frameScore[i - 1] += ((frameList[i])[0] + (frameList[i])[1])

        elif (i != 0) and frameScore[i - 1] == 10:
            frameScore[i - 1] += (frameList[i])[0]

        for j in range(len(frameList[i])):
            frameScore[i] += (frameList[i])[j]

    for i in range(len(frameScore)):
        score += frameScore[i]

    return score

def testBowlingScore():
    print("Testing bowlingScore()...", end="")
    assert((bowlingScore([1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                          6, 4 , 10, 10, 10, 10, 10, 10])) == 176)
    assert(bowlingScore([10, 10, 10, 10, 10, 10, 10, 10,
                        10, 10, 10, 10]) == 300)
    assert(bowlingScore([5, 0, 5, 2, 7, 2, 0, 4, 6, 3, 0,
                         6, 7, 3, 2, 1, 4, 6, 2, 2]) == 71)
    assert(bowlingScore([3, 5, 3, 2, 6, 3, 1, 9, 7, 2, 10,
                         4, 1, 1, 5, 0, 5, 6, 3]) == 88)
    assert(bowlingScore([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0)
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testBowlingScore()

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