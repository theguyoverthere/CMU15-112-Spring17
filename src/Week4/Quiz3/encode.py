def getPasswordString(s, pwd):
    pwdString = str(pwd)

    if len(pwdString) < len(s):
        for i in range(len(s) - len(pwdString)):
            pwdString += pwdString[i]

    return pwdString

def encode(s, pwd):
    password = getPasswordString(s, pwd)
    result = ""

    for i in range(len(s)):
        if ord(s[i])+ int(password[i]) < ord('z'):
            result += chr(ord(s[i])+ int(password[i]))
        else:
            result += chr(ord('a') + ord(s[i]) -
                          ord('z') + int(password[i]) - 1)

    return result

print(encode('abyzc',	234))
