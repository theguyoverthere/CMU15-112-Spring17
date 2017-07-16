# # 1. Sets are unordered
#
# s = set([2, 4, 8])
# print(s)
#
# for element in s:
#     print(element)
# print("---------------")
#
# # 2. Elements are unique
# s = set([2, 4, 8, 2])
# print(s)
# print(len(s))
# print("---------------")
#
# # 3. Elements must be immutable
# a = ["lists", "are", "mutable"]
# # s = set([a]) #TypeError: unhashable type: 'list'
# # print(s)
# print("---------------")
#
# # 3. Sets are mutable too.
# s1 = set(["sets", "are", "mutable", "too"])
#
# #List of set elements.
# print([s1]) #Legal
#
# # s2 = set([s1]) #TypeError: unhashable type: 'list'
# # print(s2)

# 4. Sets are very efficient
import time
n = 10000

# Create a list [2,4,6,...,n] then check for membership
# among [1,2,3,...,n] in that list.

# don't count the list creation in the timing
a = list(range(2 ,n + 1, 2))

print("Using a list...", end="")
start = time.time()
count = 0
for x in range(n + 1):
    if x in a:
        count += 1

end = time.time()
elapsed1 = end - start
print("count = ", count, "and time = %0.4f seconds" % elapsed1)

# Repeat, using a set
print("Using a set...", end="")
start = time.time()
s = set(a)
count = 0

for x in range(n + 1):
    if x in s:
        count += 1

end = time.time()
elapsed2 = end - start
print("count = ", count, "and time = %0.4f seconds" % elapsed2)

print("With n=%d, sets ran about %0.1f times faster than lists!" %
      (n, elapsed1/elapsed2))
print("Try a larger n to see an even greater savings!")
