def digitSum(n):
    n = abs(n)

    if n == 0:
        return 0
    else:
        return n % 10 + digitSum(n // 10)

assert(digitSum(123) == 1 + 2 + 3)
assert(digitSum(-1234) == 1 + 2 + 3 + 4)
