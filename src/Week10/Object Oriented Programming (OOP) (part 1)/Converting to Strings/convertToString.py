class A(object):
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "A(%d)" %self.x

    def __repr__(self):
        return "A(%d)" % self.x

a = A(5)
print(a)
print([a])

