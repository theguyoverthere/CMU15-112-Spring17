# 2d lists do not have to be rectangular
a = [ [ 1, 2, 3 ] ,
      [ 4, 5 ],
      [ 6 ],
      [ 7, 8, 9, 10 ] ]

rows = len(a)
for row in range(rows):
    columns = len(a[row]) # now cols depends on each row
    print("Row", row, "has", columns, "columns: ", end="")
    for column in range(columns):
        print(a[row][column], " ", end="")
    print()
