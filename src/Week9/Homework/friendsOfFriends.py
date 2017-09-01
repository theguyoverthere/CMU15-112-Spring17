#******************************************************************************#
# Author: Tarique Anwer
# Date:   21/8/2017
# Description: Background: we can create a dictionary mapping people to sets of
#              their friends. For example, we might say:
#
#              d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
#              d["wilma"] = set(["fred", "betty", "dino"])
#
#              With this in mind, write the function friendsOfFriends(d) that
#              takes such a dictionary mapping people to sets of friends and
#              returns a new dictionary mapping all the same people to sets of
#              their friends of friends. For example, since wilma is a friend of
#              fred, and dino is a friend of wilma, dino is a friend-of-friend
#              of fred.
#              This set should exclude any direct friends, so even though betty
#              is also a friend of wilma, betty does not count as a
#              friend-of-friend of fred (since she is simply a friend of fred).
#              Thus, in this example, if fof = friendsOfFriends(d), then
#              fof["fred"] is a set containing just "dino" and fof["wilma"] is a
#              set containing both "barney" and "bam-bam". Also, do not include
#              anyone either in their own set of friends or their own set of
#              friends-of-friends.
#              Note: you may assume that everyone listed in any of the friend
#              sets also is included as a key in the dictionary. Also, do not
#              worry about friends-of-friends-of-friends.
#******************************************************************************#

def friendsOfFriends(d):
    """ The function takes a dictionary mapping people to sets of friends and
    returns a new dictionary mapping all the same people to sets of their
    friends of friends. This set excludes any direct friends. The result also
    does not include anyone either in their own set of friends or their own set
    of friends-of-friends*.

    :param d: Dictionary mapping of people to their set of friends.
    :return: Dictionary mapping of people to their set of friend-of-friends.
    """

    result = dict()

    for people in d:
        # Not that this was specified, but some people are lonely :(
        if not d[people]:
            result[people] = set()
        else:
            for friend in d[people]:
                if friend in d:
                    for friendOfFriend in d[friend]:
                        if ((friendOfFriend not in d[people]) and
                                (friendOfFriend != people)):
                            if people in result:
                                result[people].add(friendOfFriend)
                            else:
                                result[people] = set([friendOfFriend])

    return result
