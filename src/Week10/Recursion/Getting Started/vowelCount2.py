def vowelCount2(s):
    if s == "":
        return 0
    elif len(s) == 1: return 1 if (s[0].upper() in "AEIOU") else 0
    else:
        mid = len(s)//2
        return vowelCount2(s[:mid]) + vowelCount2(s[mid:])

assert(vowelCount2("I am reeeallly happy!!! :-)") == 7)
print("ok!")