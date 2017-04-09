def letterCount(s):
    counts = [0] * 26

    for ch in s.upper():
        if (ch >= 'A') and (ch <= 'Z'):
            counts[ord(ch) - ord("A")] += 1

    return counts

def isAnagram(s1, s2):
    if letterCount(s1) == letterCount(s2):
        return True
    return False

def isAnagram2(s1, s2):
    return sorted(list(s1.upper())) == sorted(list(s2.upper()))

def testIsAnagram():
    print("Testing isAnagram()...", end="")
    assert(isAnagram("", "") == True)
    assert(isAnagram("abCdabCd", "abcdabcd") == True)
    assert(isAnagram("abcdaBcD", "AAbbcddc") == True)
    assert(isAnagram("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

def testIsAnagram2():
    print("Testing isAnagram()...", end="")
    assert(isAnagram2("", "") == True)
    assert(isAnagram2("abCdabCd", "abcdabcd") == True)
    assert(isAnagram2("abcdaBcD", "AAbbcddc") == True)
    assert(isAnagram2("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

testIsAnagram()
testIsAnagram2()
