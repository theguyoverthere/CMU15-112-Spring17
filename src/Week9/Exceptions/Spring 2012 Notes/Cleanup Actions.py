#1) Wrong Way

filename = "non-existent-file.txt"
try:
    file = open(filename, "r")
    print(filename, "has", len(file.readlines()), "lines")
except IOError:
    print("1. Cannot open file,", filename)
finally:
    # file.close() #Error, file not defined here!
    pass

# 2) The Right Way!

filename = "non-existent-file.txt"
file = None
try:
    file = open(filename, "r")
    print(filename, "has", len(file.readlines()), "lines")
except IOError:
    print("2. Cannot open file,", filename)
finally:
    if file: file.close()
    