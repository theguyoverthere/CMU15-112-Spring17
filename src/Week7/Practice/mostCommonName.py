#******************************************************************************#
# Author: Tarique Anwer
# Date:   25/7/2017
# Function: Takes a list of names (such as ['Jane', 'Aaron', 'Cindy', 'Aaron'],
#           and returns the most common name in this list (in this case,
#           'Aaron'). If there is more than one such name, return a set of the
#           most common names. So mostCommonName(['Jane', 'Aaron', 'Jane',
#          'Cindy', 'Aaron']) returns the list ['Aaron', 'Jane']. If the set is
#           empty, return None. Also, treat names case sensitively, so 'jane'
#           and 'Jane' are different names.
# Args:     a: A list of strings.
# Returns:  A list of strings or None
# Raises:   NA
#******************************************************************************#

def mostCommonName(a):
    if not a: return None

    maxCount = 0
    result = set()
    nameCount = {}

    # Create the nameCount Dictionary
    for i in range(len(a)):                    #O(N)
        if a[i] in nameCount:                  # O(1)
            nameCount[a[i]] += 1               # O(1)
            if nameCount[a[i]] > maxCount:     # O(1)
                maxCount = nameCount[a[i]]     # O(1)
        else:                                  # O(1)
            nameCount[a[i]] = 0                # O(1)

    # Generate the result set
    for name in nameCount:                     #O(N)
        if nameCount[name] == maxCount:        # O(1)
            result.add(name)                   # O(1)

    return result                              # O(1)
