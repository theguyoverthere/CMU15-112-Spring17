# A few example recursive functions.
# Can you figure out what each one does, in general?

import math

def f1(x):
    if x == 0: return 0
    else: return 1 + f1(x-1) #f(0) = 0, f(1) = 1, f(2) = 2, f(3) = 3

def f2(x):
    if x == 0: return 40
    else: return 1 + f2(x-1) #f(0) = 40, f(1) = 41, f(2) = 42

def f3(x):
    if x == 0: return 0
    else: return 2 + f3(x-1) #f(0) = 0, f(1) = 2, f(2) = 4, f(3) = 6

def f4(x):
    if x == 0: return 40
    else: return 2 + f4(x-1) #f(0) = 42, f(1) = 42, f(2) = 44, f(3) = 46

def f5(x):
    if x == 0: return 0      #Triangular Numbers
    else: return x + f5(x-1) #f(0) = 0, f(1) = 1, f(2) = 3, f(3) = 6

def f6(x):
    if x == 0: return 0
    else: return 2*x-1 + f6(x-1) #f(0) = 0, f(1) = 1, f(2)= 4, f(3) = 9
    # (x - 1)** 2 = x**2 - 2 * x + 1
    # 2 *x - 1 + (x -1) ** 2 = x ** 2

def f7(x):
    if x == 0: return 1
    else: return 2*f7(x-1) #f(0) = 1, f(1) = 2, f(2) = 4 , f(3) = 8, f(4) = 16

def f8(x):
    if x < 2: return 0
    else: return 1 + f8(x//2) #f(0) = 1, f(1) = 0, f(2) = 1, f(4) = 2, f(8) = 3

def f9(x):
    if x < 2: return 1
    else: return f9(x-1) + f9(x-2) #Fibonacci Numbers

def f10(x):
    if x == 0: return 1 # Factorials!
    else: return x*f10(x-1) #f(0) = 1, f(1) = 1, f(2) = 2, f(3) = 6, f(4) = 24

def f11(x, y):
    if y < 0: return -f11(x, -y)
    elif y == 0: return 0
    else: return x + f11(x, y-1) #f(2,3) = 2 + f(2, 2)
                                 #       = 2 + 2 + f(2, 1)
                                 #       = 2 + 2 + 2 + f(2, 0)
                                 #       = 2 + 2 + 2 + 0
                                 #       = 6

def f12(x,y):
    if (x < 0) and (y < 0): return f12(-x,-y)
    elif (x == 0) or (y == 0): return 0
    else: return x+y-1 + f12(x-1, y-1)  #Returns product of x and y
# (x - 1)*(y - 1) = x * y - (x + y - 1)

def f13(L):
    assert(type(L) == list)
    if len(L) < 2: return [ ]
    else: return f13(L[2:]) + [L[1]] # [0, 1, 2, 3, 4, 5] ---> [5, 3, 1]
                                     # [2, 3, 4, 5] ---> [5, 3]
                                     # [4, 5] ---> [] + [5] = [5]
                                     # [] ---> []
def go():
    while True:
        n = input("Enter function # (1-13, or 0 to quit): ")
        if n == "0": break
        elif n == "11": print("f11(5, 7) ==", f11(5, 7))
        elif n == "12": print("f12(5, 7) ==", f12(5, 7))
        elif n == "13": print("f13(list(range(20)) ==", f13(list(range(20))))
        else:
            f = globals()["f"+n]
            print("f"+n+": ", [f(x) for x in range(10)])
        print()

go()