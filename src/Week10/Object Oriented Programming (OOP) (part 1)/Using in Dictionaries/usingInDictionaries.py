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

d = dict()
d[A(5, 4)] = 42

print(d[A(5, 4)])
