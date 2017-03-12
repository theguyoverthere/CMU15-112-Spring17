def ct1(x, y, z):
    count = 0
    while x > y:
        x //= 2
        y -= z
        z += 1
        print(x, end=' ')
        print(y, end=' ')
    return z

print(ct1(20, 10, 2)) # prints 5 values

def ct2(x):
    y = 3
    while True:
        print(y, end=' ')
        for z in range(1, x*y, 2):
            if z % 3 == 1:
                print(z, end=' ');
                continue
            y += x
            if y % 5 > 0:
                print(y, end=' ')
                break
            print(y, end=' ')
        if y > 10: return x
        y += 1

print(ct2(7)) # prints 5 values

def rc1(n):
     if n == 0: return False
     count = 0
     for x in range(0, 100, n):
        count += 1
     # hint: here, x equals the last value in the range
     return (count == 5) and (x//10 == x%10 + 4)

print(rc1(21))


def isDecreasingOddsNumber(n):
   previousDigit = 0

   while n > 0:
      nthDigit = n % 10

      if (nthDigit % 2 == 0) or (nthDigit <= previousDigit):
          return False

      n //= 10
      previousDigit = nthDigit

   return True

def nthDecreasingOddsNumber(n):
      found = 0
      guess = 0

      while found <= n:
         guess += 1
         if isDecreasingOddsNumber(guess):
             found += 1

      return guess

# for i in range(100):
#     print(nthDecreasingOddsNumber(i))

import math

def almostEqual(d1, d2, epsilon=10**-7):
    return abs(abs(d2-d1) < epsilon)

def f(x): return x/2 + 0.5

def latticePointCount(f, x1, x2):
    lowerBound = math.ceil(x1)
    upperBound = math.floor(x2)
    latticeCount = 0

    for x in range(lowerBound, upperBound + 1):
        if almostEqual(f(x), math.floor(f(x))):
            latticeCount += 1

    return latticeCount

print(latticePointCount(f, 0.8, 4.7))

def bonusCt1(x, y=0):
   def f(x):
      for y in range(x):
          x += 2*y
      return x

   for x in range(f(x), f(f(x)), x):   #x in (9, 81, 3)
      if x%10 + x//10 > 13:
          y = 100*y + x

   return y

print(bonusCt1(3))