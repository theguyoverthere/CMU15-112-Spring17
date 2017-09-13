def interleave(list1, list2):

    if len(list1) == 0:
        return []
    elif len(list1) == 1:
        return [list1[0], list2[0]]
    else:
        mid = len(list1) // 2
        return (interleave(list1[:mid], list2[:mid]),
                interleave(list1[mid:], list2[mid:]))

print(interleave([1, 2, 3], [4, 5, 6]))

# mid = 1
# return (interleave(list1[1], list2[4]),            --- Recursion A
#         interleave(list1[2, 3], list2[5, 6]))      --- Recursion B

