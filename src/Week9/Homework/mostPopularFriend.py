#******************************************************************************#
# Author: Tarique Anwer
# Date:   05/8/2017
# Description: Recall that friendsOfFriends(d) takes a dictionary d like this:
#              d = dict()
#              d["fred"] = set(["wilma", "betty", "barney"])
#              d["wilma"] = set(["fred", "betty", "dino"]) With this in mind,
#              write the function mostPopularFriend(d) that takes a dictionary
#              of that form, and returns the name that occurs the most number of
#              times in all the sets of friends. In the example above,
#              mostPopularFriend(d) would return "betty". You may assume that
#              there is exactly one such name, so ignore ties.
#******************************************************************************#

def mostPopularFriend(d):
    nameCount = dict()
    mostPopular = ""
    count = 0

    for key in d:
        for name in d[key]:
            if name in nameCount:
                nameCount[name] += 1
            else:
                nameCount[name] = 1

    for name in nameCount:
        if nameCount[name] > count:
            count = nameCount[name]
            mostPopular = name

    return mostPopular

d = dict()
d["fred"] = set(["wilma", "betty", "barney"])
d["wilma"] = set(["fred", "betty", "dino"])

print(mostPopularFriend(d))