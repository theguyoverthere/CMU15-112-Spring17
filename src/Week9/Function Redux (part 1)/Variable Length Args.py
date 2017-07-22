def longestWord(*args):
    if len(args) == 0: return None

    result = args[0]

    for word in args:
        if (len(word)) > len(result):
            result = word

    return result

print(longestWord("this", "is", "really", "nice", "elephant"))

myWords = ["this", "is", "really", "nice", "elephant"]
print(longestWord(*myWords))



