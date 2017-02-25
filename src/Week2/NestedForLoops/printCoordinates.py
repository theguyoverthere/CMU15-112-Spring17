def printCoordinates(xMax, yMax):
    for x in range(xMax + 1):
        for y in range(yMax + 1):
            print("(", x, ",", y, ")")
        print()

printCoordinates(4, 5)