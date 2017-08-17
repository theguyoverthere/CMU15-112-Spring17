#******************************************************************************#
# Author: Tarique Anwer
# Date:   17/8/2017
# Description: Write the function invertDictionary(d) that takes a dictionary d
#              that maps keys to values and returns a dictionary of its inverse,
#              that maps the original values back to their keys. One
#              complication: there can be duplicate values in the original
#              dictionary. That is, there can be keys k1 and k2 such that
#              (d[k1] == v) and (d[k2] == v) for the same value v. For this
#              reason, we will in fact map values back to the set of keys that
#              originally mapped to them. So, for example:
#              assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) ==
#                           {2:set([1]), 3:set([2,5]), 4:set([3])})
#******************************************************************************#
def invertDictionary(d):
    result = dict()

    for key in d:
        value = d[key]

        if value in result:
            result[value].add(key)
        else:
            result[value] = set([key])

    return result
