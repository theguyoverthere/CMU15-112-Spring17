class A(object):
    pass

a = A()
print(type(A))
print(type(a) == A)
print(isinstance(a, A))
print(isinstance(a, str))