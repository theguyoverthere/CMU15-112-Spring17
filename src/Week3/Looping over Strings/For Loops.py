# 1. "For" loop with indexes
s = "abcd"
for i in range(len(s)):
    print(i, s[i])
print("-----------")

# 2. "For" loop without indexes
s = "abcd"
for c in s:
    print(c)
print("-----------")

# 3. "For" loop with split
names = "Fred,Wilma,Betty,Barney"
for name in names.split(","):
    print(name)
print("-----------")

# 4. "For" loop with splitlines
# quotes from brainyquote.com
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if line.startswith("Knuth"):
        print(line)