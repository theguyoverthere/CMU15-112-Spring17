def letterCount(s):
    counts = dict()

    for ch in s.upper():
        if (ch >= 'A' ) and (ch <= 'Z'):
            counts[ch] = 1 + counts.get(ch, 0)

    return counts

def isAnagram(s1, s2):
    return letterCount(s1) == letterCount(s2)


def testIsAnagram():
    print("Testing isAnagram()...", end="")
    assert(isAnagram("", "") == True)
    assert(isAnagram("abCdabCd", "abcdabcd") == True)
    assert(isAnagram("abcdaBcD", "AAbbcddc") == True)
    assert(isAnagram("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

testIsAnagram()
