from src.Week9.Practice.mergeSortWithOneAuxList import mergeSortWithOneAuxList
from src.Week9.Sorting.mergeSort import mergeSort

import random
import time

def testSort(sortFn, n):
    a = [random.randint(0,2**31) for i in range(n)]
    sortedA = sorted(a)
    startTime = time.time()
    sortFn(a)
    endTime = time.time()
    elapsedTime = endTime - startTime
    assert(a == sortedA)
    print("%20s n=%d  time=%6.3fs" % (sortFn.__name__, n, elapsedTime))

def testSorts():
    n = 2**20 # use 2**8 for Brython, use 2**12 or larger for Python
    for sortFn in [mergeSort, mergeSortWithOneAuxList]:
        testSort(sortFn, n)

testSorts()
