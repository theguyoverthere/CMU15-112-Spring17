# Default args example:
#---------------------------#
def f(x, y=10): return x, y
print(f(5))   # (5, 10)
print(f(5,6)) # (5, 6)
print()

# Do not use mutable default args
#---------------------------#
def f1(x, L=[ ]):
    L.append(x)
    return L

print(f1(1))
# See the link below for explanation:
# https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument#
# http://effbot.org/zone/default-values.htm
print(f1(2)) # why is this [1, 2]?
print()

# One workaround for mutable default args
#---------------------------#
def f2(x, L=None):
    if L is None:
        L = [ ]
    L.append(x)
    return L

print(f2(1))
print(f2(2)) # [2] (that's better)
