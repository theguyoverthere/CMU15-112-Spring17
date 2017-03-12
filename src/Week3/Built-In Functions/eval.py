# eval() works but you should not use it!
s = "(3 ** 2 + 4 ** 2) ** 0.5"
print(eval(s))

def reformatMyHardDrive():
    return 0

# why not? Well...
s = "reformatMyHardDrive()"
print(eval(s)) # no such function!  But what if there was?