def rangeSum(lo, hi):
    if lo > hi:
        return 0
    else:
        return lo + rangeSum(lo + 1, hi)

print(rangeSum(10,15)) # 75