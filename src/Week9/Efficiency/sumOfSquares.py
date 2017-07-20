# The following functions all solve the same problem:
# Given a non-negative integer n, return True if n is the sum
# of the squares of two non-negative integers, and False otherwise.

def f1(n):
    for x in range(n + 1):
        for y in range(n + 1):
            if x ** 2 + y ** 2 == n:
                return True
    return False

def f2(n):
    for x in range(n + 1):
        for y in range(x, n + 1):
            if x ** 2 + y ** 2 == n:
                return True
    return False

def f3(n):
    xMax = int(n**0.5)

    for x in range(xMax + 1):
        for y in range(x, n + 1):
            if x ** 2 + y ** 2 == n:
                return True

    return False

def f4(n):
    xyMax = int(n**0.5)

    for x in range(xyMax + 1):
        for y in range(x, xyMax + 1):
            if x ** 2 + y ** 2 == n:
                return True

    return False

def f5(n):
    xyMax = int(n**0.5)

    for x in range(xyMax + 1):
        y = int((n - x ** 2) ** 0.5)

        if x ** 2 + y ** 2 == n:
            return True

    return False

def testFunctionsMatch(maxToCheck):
    # first, verify that all 5 functions work the same

    print("Verifying that all functions work the same...")
    for n in range(maxToCheck):
        assert(f1(n) == f2(n) == f3(n) == f4(n) == f5(n))

    print("All functions match up to n =", maxToCheck)

testFunctionsMatch(1000) # use larger number to be more confident

import time
def timeFnCall(f, n):
    # call f(n) and return time in ms
    # Actually, since one call may require less than 1 ms,
    # we'll keep calling until we get at least 1 secs,
    # then divide by # of calls we had to make
    calls = 0
    start = end = time.time()
    while (end - start < 1):
        f(n)
        calls += 1
        end = time.time()
    return float(end - start)/calls*1000 #(convert to ms)

def timeFnCalls(n):
    print("***************")
    for f in [f1, f2, f3, f4, f5]:
        print ("%s(%d) takes %8.3f milliseconds" %
               (f.__name__, n, timeFnCall(f, n)))

timeFnCalls(1001)  # use larger number, say 3000, to get more accurate timing