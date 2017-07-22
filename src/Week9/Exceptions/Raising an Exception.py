def lastChar(s):
    if len(s) == 0:
        # This is (a simple form of) how you raise your own custom exception.
        raise Exception("String must be non-empty!")
    else:
        return s[-1]


print(lastChar("abc"))
print(lastChar(""))
print("This line will never print!")
