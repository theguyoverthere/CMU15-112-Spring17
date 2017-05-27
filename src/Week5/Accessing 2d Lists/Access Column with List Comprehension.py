# still a copy, still expensive, but cheaper and cleaner with a list comprehension!
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]

rows, columns = len(a), len(a[0])
column = 1

colList = [ a[row][column] for row in range(rows) ]
print(colList)
