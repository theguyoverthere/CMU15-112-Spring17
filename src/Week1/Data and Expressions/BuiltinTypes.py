import math


def f():
    print("This is a user defined function")
    return 42


print("Some basic function types:")
print(type(2))                # int
print(type(2.2))              # float
print(type("2.2"))            # str (string)
print(type(2 < 2.2))          # bool (boolean)
print(type(math))             # module
print(type(math.tan))         # builtin_function_or_method("function" in brython)
print(type(f))                # function (user-defined function)
print(type(type(42)))         # type

print("##########################################")

print("And some other types we will see later in the course..")
print(type(Exception()))      # exception
print(type(range(5)))         # range

print(type([1, 2, 3]))        # list
print(type((1, 2, 3)))        # tuple
print(type({1, 2, 3}))        # set

print(type({1: 42}))          # dict (dictionary or map)
print(type(2 + 3j))           # complex (complex numbers) (we may not see this type)
