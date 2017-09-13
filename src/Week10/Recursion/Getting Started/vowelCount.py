def vowelCount(s):
    if len(s) == 0:
        return 0
    else:
        thisCount = 1 if (s[0].upper() in "AEIOU") else 0
        restCount = vowelCount(s[1:])
        return thisCount + restCount

assert(vowelCount("I am reeeallly happy!!! :-)") == 7)
assert(vowelCount("L") == 0)
print("ok")

s = "This works!"
print(vowelCount(s)) # 2
L = list(s)
print(vowelCount(L)) # crash! IndexError: list index out of range