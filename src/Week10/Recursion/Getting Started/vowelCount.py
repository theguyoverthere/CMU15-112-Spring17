def vowelCount(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return s[0].upper() in "AEIOU"
    else:
        thisCount = vowelCount(s[0])
        restCount = vowelCount(s[1:])
        return thisCount + restCount

assert(vowelCount("") == 0)
assert(vowelCount("I am reeeallly happy!!! :-)") == 7)
print("ok!")