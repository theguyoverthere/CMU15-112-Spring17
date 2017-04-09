def onesDigit(n):
    return n%10

def ct1(L):
    for i in range(len(L)):
        L[i] += sum(L) + max(L)

    # The function onesDigit is called on each element before
    # making comparison.
    return sorted(L, key=onesDigit)

a = [2,1,0]
print(ct1(a))
print(a)
