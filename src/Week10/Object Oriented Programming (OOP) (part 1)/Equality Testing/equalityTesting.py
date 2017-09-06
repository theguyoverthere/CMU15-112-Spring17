class A(object):
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, A) and (self.x == other.x)

a1 = A(5)
a2 = A(5)
print(a1 == a2) #obj1 == obj2 --> obj1.__eq__(obj2)
print(A(5) == A(7))
print(A(4) == 9)


