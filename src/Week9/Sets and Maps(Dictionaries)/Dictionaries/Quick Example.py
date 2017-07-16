# Example 1:
stateMap = {'pittsburgh':'PA', 'chicago':'IL', 'seattle':'WA', 'boston':'MA'}
city = input("Enter a city name --> ").lower()
if city in stateMap:
    print(city.title(), "is in", stateMap[city])
else:
    print("Sorry, never heard of it.")

# Example 2:
counts = dict()

while True:
    n = int(input("Enter an integer (0  to end) -->"))
    if n == 0: break
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

    print("I have seen", n, "a total of", counts[n], "time(s)")
print("Done counts:", counts)

