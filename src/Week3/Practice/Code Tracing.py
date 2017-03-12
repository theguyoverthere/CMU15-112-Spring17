def ct1(s, t):
    result = ""
    for c in  s:
        if c.upper() not in  "NO!!!":
            i = t.find(c)
            if result != "": result += ":"
            result += "%d%s%s%s" % (i, c, s[i], t[i])
    return result
print(ct1("net",   "two"))

def ct2(s):
    result = ""
    d = ord("a")
    for c in s.lower():
        if  c.isalpha() and (ord(c) >= d):
            result += str(ord(c) - d) + chr(d)
            d += 1
    return result

print(ct2("Be a CA?!?"))

def ct3(s):
    result = ""
    while len(s) > 1:
        result += s[:1] + s[2:4] + "."
        s = s[1:-1:2]
    return result + s
print(ct3("abcdefghi"))


def rc1(s):
    if not isinstance(s, str): return  False
    if '0' in  s: return  False
    t, n = s[1:-1], int(s[0]+s[-1])

    return t.isalpha() and (t == t[0]*(n//2))

# t must be alphabetic. s must be a string. 's' does not have '0' anywhere inside
# t = s[1:-1] i.e a copy of s with the first character removed -- Hint.
# Since t.isalpha() is true, the last character cannot be a numeric digit,
# but the first character can be.
# n = int(first and last characters concatenated)
# s[0] = 2 s[-1] = ' ' n = 2
# s = '2a '

print(rc1('2a '))


def rc2(s, t):
    assert((s !=  "") and (t != "") and (s in t) and (s != t))
    result =  ""
    for i in range(len(s)):
        if (i % 2) == 0: result += t[i]
        else: result += t[-1-i]
    return result == s


# result = s ..(i)
# s and t are not null ...(ii)
# s is a substring of t
# Lets say s = "ab" , t = "abc" i in range(2):
# i = 0 -> result = 'a'
# i = 1 -> result = 'ab'

print(rc2('ab', 'abc'))
