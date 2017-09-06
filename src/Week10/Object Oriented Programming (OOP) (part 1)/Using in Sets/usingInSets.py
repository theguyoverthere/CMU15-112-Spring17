class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, A) and
                (self.x == other.x)  and
                (self.y == other.y))

    def getHashables(self):
        return self.x, self.y

s = set()
s.add(A(5, 2))
print(A(5, 2) in s)

a = A(5, 2)
s.add(a)
print(a in s)