def isTinyPal(n):
   if isinstance(n, int) and (n > -1000) and (n < 1000):
       if (abs(n) > 9) and (abs(n) < 100):   # two digit number
           leftMostDigit = abs(n) // 10
       else:
           leftMostDigit = abs(n) // 100

       righMostDigit = abs(n) % 10

       if (abs(n) < 10) or (leftMostDigit == righMostDigit): return True
   return False

print(isTinyPal(80009))  #returns False # not a palindrome
print(isTinyPal(80008))  #returns False # not tiny
print(isTinyPal(8000.8)) # returns False # not an int
print(isTinyPal("80008"))# returns False # not an int
print(isTinyPal(809))  #returns False # not a palindrome
print(isTinyPal(808))  #returns True
print(isTinyPal(121)) # returns True
print(isTinyPal(11))  # returns True
print(isTinyPal(1))   # returns True

print(isTinyPal(-808))  #returns True
print(isTinyPal(-121)) # returns True
print(isTinyPal(-11))  # returns True
print(isTinyPal(-1))   # returns True

def bonusCt2(x, y):
   return (x + bonusCt2(x - 1, y - 1) if (y > 0) else
          (2 + bonusCt2(x - 1, y) if (x > 0) else 42))
print(bonusCt2(7, 4))
