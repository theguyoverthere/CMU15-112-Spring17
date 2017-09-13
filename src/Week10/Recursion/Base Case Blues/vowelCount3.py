def vowelCount3(s):
    # same as above...
    # if s == "": return 0
    if len(s) == 0: return 0
    else:
        thisCount = 1 if (s[0].upper() in "AEIOU") else 0
        restCount = vowelCount3(s[1:])
        return thisCount + restCount

s = "This works!"
print(vowelCount3(s)) # 2
L = list(s)
print(vowelCount3(L)) # crash! IndexError: list index out of range