# 1. Length of the string = N. Therefore number of steps involved is
# 1 + N(N + 1 + 1 + 2) = 1 + N(N + 4) = N ** 2 + 4 N + 1 = O(N**2)

def bigOh1(s):
    charCount=""                      #O(1)
    for c in s:                       #O(N)
        count = s.count(c)            #O(N) + 1
        if c in charCount:            #O(1)
            continue                  #O(1)
        else:
            charCount += "%s%d " % (c, count) #O(1)

# 2. Length of the string = N. Therefore number of steps involved is
#  N**2 + 1 + 1 + N**2(N + 2) = N**3 + 3N**2 + 2 = O(N**3)

def bigOh2(s):
    myS = s * len(s)                  #O(N**2)
    result = ""                       #O(1)
    for c in myS:                     #O(N**2)
        if c in result:               #O(N)
           break                      #O(1)
        else:
            result += c               #O(1)
    return result                     #O(1)

# 3. Length of the string = N. Therefore number of steps involved is
#  N(1 + 2N)  + N = 2N**2 + N + N = 2N**2 + 2N = O(N**2)

def bigOh3(a):
    for i in range(len(a)):            #O(N)
        j=1                            #O(1)
        while j < len(a):              #O(N)
            j *= 2                     #(1)
    print(a)                           #(N)

# 4. Length of the List = N. Therefore number of steps involved is
#  4 + N logN = NlogN

# 4 + N/4**0(N/4**0 + 3)   - No of steps in 1st Pass
# 4 + N/4**1(N/4**1 + 3)   - No of steps in 2nd Pass
# 4 + N/(4**2)(N/4**2 + 3) - No of steps in 3rd Pass
# ----------------------
# 4 + N/(4**k)(N/4**k + 3) - No of steps in kth Pass
#
# N / 4 ** k = 1
# 4 ** k = N
# k log 4 = log N
# k = log N/ log 4  <<-- No of steps evaluated
# The loop actually ends after evaluating one more step.

def bigOh4(L):
    # assume L is a 1d list
    N = len(L)                         #O(1)
    n = len(L)                         #O(1)
    while n > 0:                       #O(logN)
        print(max(L[0:N]))             #O(N)
        n //= 4                        #O(1)

# 5. Length of the List = N. Therefore number of steps involved is
#  1 + N(N(N + 1) / 2) = 1 + (N**3 + N**2) / 2 = O(N**3)

def bigOh5(L):
    # assume L is a 1d list
    N = len(L)                                  #O(1)
    for i in range(N):                          #O(N)
        for j in range(i, N):
            if (L[i] > L[j]):
                (L[i], L[j]) = (L[j], L[i])
