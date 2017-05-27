# copy (not an alias!); expensive (new list created)
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]

rows, columns = len(a), len(a[0])
column = 1
colList = [ ]

for row in range(rows):
    colList += [ a[row][column] ]
print(colList)
