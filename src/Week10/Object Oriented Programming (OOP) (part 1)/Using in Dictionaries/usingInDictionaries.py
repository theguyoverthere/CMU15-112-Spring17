class A(object):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, A) and
                (self.x == other.x))

    def getHashables(self):
        return self.x

d = dict()
d[A(5)] = 42

print(d[A(5)])
