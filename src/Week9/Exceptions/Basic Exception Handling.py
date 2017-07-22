print("This is a demonstration of the basic try/except.")
try:
    print("Here we are just before the error!")
    print("1/0 equals:", (1/0))
    print("This line will never run!")
except:
    print("**We caught an error**")
print("And that concludes our demonstration")
