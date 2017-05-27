# Create an "arbitrary" 2d List
a = [ [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 0],
      [3, 4, 5, 6, 7]
    ]

print("Before: a =", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])

# And now loop over every element
# Here, we'll add one to each element,
# just to make a change we can easily see
for row in range(rows):
    # For even rows and odd columns, increment value by 1
    if row % 2 == 0:
        for col in range(cols):
            if col % 2 == 1:
                a[row][col] += 1

# Finally, print the results
print("After:  a =", a)
