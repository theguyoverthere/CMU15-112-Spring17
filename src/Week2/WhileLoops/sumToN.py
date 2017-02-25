# sum numbers from 1 to 10

# note:  this works, but you should not use "while" here.
#        instead, do this with "for" (once you know how)

def sumToN(n):
    total = 0
    counter = 1

    while counter <= n:
        total += counter
        counter += 1

    return total

print(sumToN(5) == 1 + 2 + 3 + 4 + 5)


# A for loop is the preferred way to loop over a fixed range.
def sumToN(n):
    total = 0

    for counter in range(n+1):
        total += counter
    return total

print(sumToN(5) == 1 + 2 + 3 + 4 + 5)
