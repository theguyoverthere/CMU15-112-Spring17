from src.Week9.Sorting.mergeSort import *
from src.Week9.Sorting.builtinSort import *
from src.Week9.Sorting.bubbleSort import *
from src.Week9.Sorting.selectionSort import *

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
    n = 2**14 # use 2**8 for Brython, use 2**12 or larger for Python
    for sortFn in [selectionSort, bubbleSort, mergeSort, builtinSort]:
        testSort(sortFn, n)

testSorts()
