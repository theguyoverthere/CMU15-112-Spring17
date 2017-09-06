class A(object):
    def __init__(self, color, isHappy):
        self.color = color
        self.isHappy = isHappy


a1 = A('yellow', True)
a2 = A('blue', False)

print(a1.color, a1.isHappy)
print(a2.color, a2.isHappy)
