filename = "non-existent-file.txt"
try:
    #using 'with', no need for file.close in finally
    with open(filename, "r") as file:
        print(filename, "has", len(file.readlines()), "lines")
except IOError:
    print("Cannot open file,", filename)


