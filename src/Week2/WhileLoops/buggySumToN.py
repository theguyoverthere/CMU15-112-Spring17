def buggySumToN(n):
    total = 0
    counter = 0 # Bug alert!

    while counter <= n:
        counter += 1
        total   += counter #Bug Alert

    return total

print(buggySumToN(5) == 1  + 2 + 3 + 4 + 5)

