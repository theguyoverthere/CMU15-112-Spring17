#******************************************************************************#
# Author: Tarique Anwer
# Date:   24/4/2017
# Function: Takes a sorted wordlist and a single word (all words in this problem
#           will only contain lowercase letters). If the word is in the wordlist
#           , then that word is returned. Otherwise, the function returns a list
#           of all the words (in order) in the wordlist that can be obtained by
#           making a single small edit on the given word, either by adding a
#           letter, deleting a letter, or changing a letter. If no such words
#           exist, the function returns None.
# Args:     wordList: A list of strings
#           word: A String
# Returns:  A list of strings, or None
# Raises:   NA
#******************************************************************************#
import cs112_s17_linter

def isNearestWord(wordInList, word):

    if len(wordInList) - len(word) == 1: # Possibly addition
        if word in wordInList:
            return True

        count = 0
        while word[count] == wordInList[count]:
            count += 1
        if wordInList[count + 1:] == word[count :]:
            return True

    elif len(wordInList) - len(word) == -1: # Possibly deletion
        if wordInList in word:
            return True

        count = 0
        while word[count] == wordInList[count]:
            count += 1
        if word[count + 1:] == wordInList[count :]:
            return True

    elif len(wordInList) == len(word): # Possible Change
        if (wordInList[1 : ] == word[1 : ] or
            wordInList[: len(wordInList) - 1] == word[: len(word) - 1]):
            return True

        count = 0
        while word[count] == wordInList[count]:
            count += 1
        if wordInList[count + 1:] == word[count + 1:]:
            return True

def nearestWord(wordList, word):
    if word in wordList:
        return word

    result = []
    for i in range(len(wordList)):
        if isNearestWord(wordList[i], word):
            result.append(wordList[i])

    return result

def testAlternatingSum():
    print("Testing nearestWord()...", end="")
    assert(nearestWord([], "hi") == [])
    assert(nearestWord(["Hello", "Hellos", "Hollow"], "hi") == [])
    assert(nearestWord(["yearn", "lears", "leary"], "learn"))
    assert(nearestWord(["cello", "hallo", "hillo", "hollo" , "hullo", "helio",
                        "hells"], "hello"))
    assert(nearestWord(["choir", "charr", "chainn"], "chair"))
    assert(nearestWord(["aba", "baa", "bar", "ban", "oba"], "ba"))
    assert (nearestWord(["aba", "baa", "bar", "ban", "oba", "bxa", "bbxa"],
                        "ba"))
    assert(nearestWord(["ax"], "abx"))
    print("Passed!")
    return 0

#################################################
# testAll and main
#################################################

def testAll():
    testAlternatingSum()

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