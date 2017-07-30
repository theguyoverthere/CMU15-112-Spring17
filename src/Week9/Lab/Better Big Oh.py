import copy

"""
1. Assuming a is a list, the function counts the number of elements in a, by
   discarding elements from it, one at a time.

2. Total number of steps = 1 + N + 3N + 1 = 4N + 2 = O(N)

3. def slow1(a):
       return len(a)   #O(1)
"""
def slow1(a):
    (b, c) = (copy.copy(a), 0) #O(n)
    while (b != [ ]):          #O(n)
        b.pop()                #O(1)
        c += 1                 #O(1)
    return c                   #O(1)

"""
1. Determines if there is a duplicate item in the list. Return true if there
   are no duplicates, False otherwise.

2. Total number of steps = 2 + 5N**2 + 2 = 5N**2 + 4 = O(N**2)

3. def slow2(a):
       a.sort                          #O(NlogN)
       for i in range(1 : len(a)):     #O(N)
           if a[i] == a[i-1]:          #O(1)
              return False             #O(1)
               
       return True                     #O(1)
"""

def slow2(a):
    n = len(a)                 #O(1)
    count = 0                  #O(1)
    for i in range(n):         #O(N)
        for j in range(n):     #O(N)
            if (a[i] == a[j]): #O(1)
                count += 1     #O(1)
    return (count == n)        #O(1)

""" 
1. Returns the count of elements in the difference set b - a.

2. Total number of steps = 6 + 2N**2 = O(N**2) 

3. def slow3(a, b): 
       assert(len(a) == len(b))  #O(1)
       return len(set(b) - set(a)) #O(N)
    
"""
def slow3(a, b):
    # assume a and b are the same length n
    n = len(a)                 #O(N)
    assert(n == len(b))        #O(1)
    result = 0                 #O(1)
    for c in b:                #O(N)
        if c not in a:         #O(N)
            result += 1        #O(1)
    return result              #O(1)

"""
1. Return the maximum absolute difference between numbers in the two list. 
Difference between numbers in the same list do NOT count.

2. Total number of steps = 9 + 5N**2 = O(N**2)
3. def slow4(a, b):
       a.sort()                                        #O(NlogN)
       b.sort()                                        #O(NlogN)
       return (max(max(a) - min(b), max(b) - min(a)))  #O(N)
"""

def slow4(a, b):
    # assume a and b are the same length n
    n = len(a)                         #O(1)
    assert(n == len(b))                #O(1)
    result = abs(a[0] - b[0])          #O(1)
    for c in a:                        #O(N)
        for d in b:                    #O(N)
            delta = abs(c - d)         #O(1)
            if (delta > result):       #O(1)
                result = delta         #O(1)
    return result                      #O(1)

"""
1. Return the minimum absolute difference between numbers in the two list.

2. Total number of steps = 9 + 5N**2 = O(N**2)
import bisect

3. def slow51(a, b):
        a.sort()                                                          #O(NlogN)
        result = abs(a[0] - b[0])                                         #O(1)
    
        for i in range(len(b)):                                           #O(N) 
            j = bisect.bisect(a, b[i])                                    #O(logN)
    
            # Only one comparison to the right.
            if j == 0:                                                    #O(1)
                if abs(b[i] - a[j]) < result:                             #O(1)
                    result = abs(b[i] - a[j])                             #O(1)
    
            # Only one comparison to the left.
            elif j == len(a):                                             #O(1)
                if abs(b[i] - a[j - 1]) < result:                         #O(1)
                    result = abs(b[i] - a[j - 1])                         #O(1)
    
            # Compare on both side
            else:                                                         #O(1)
                result = min(abs(b[i] - a[j - 1]), abs(b[i] - a[j + 1]))  #O(1)
    
        return result                                                     #O(1) 
"""

def slow5(a, b):
    # Hint: this is a tricky one!  Even though it looks syntactically
    # almost identical to the previous problem, in fact the solution
    # is very different and more complicated.
    # You'll want to sort one of the lists,
    # and then use binary search over that sorted list (for each value in
    # the other list).  In fact, you should use bisect.bisect for this
    # (you can read about this function in the online Python documentation).
    # The bisect function returns the index i at which you would insert the
    # value to keep the list sorted (with a couple edge cases to consider, such
    # as if the value is less than or greater than all the values in the list,
    # or if the value actually occurs in the list).
    # The rest is left to you...
    #
    # assume a and b are the same length n
    n = len(a)

    result = abs(a[0] - b[0])
    for c in a:
        for d in b:
            delta = abs(c - d)
            if (delta < result):
                result = delta
    return result

def binarySearch(a, x):
    lower = 0
    upper = len(a) - 1
    a.sort()

    while upper - lower >= 0:
        middle = (upper + lower) // 2

        if a[middle] == x:
            return True
        elif x > a[middle]:
            lower = middle + 1
        else:
            upper = middle - 1

    return False