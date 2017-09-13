def rangeSum(lo, hi):
    if lo > hi:
        return 0
    else:
        mid = (lo + hi) // 2
        return rangeSum(lo, mid) + rangeSum(mid + 1, hi)
