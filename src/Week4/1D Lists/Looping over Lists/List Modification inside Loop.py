b = [ 2, 3, 5, 3, 7 ]
print("b =", b)

# Failed attempt to remove all the 3's
for index in range(len(b)):
    if b[index] == 3:  # this eventually crashes!
        b.pop(index)

print("This line will not run!")