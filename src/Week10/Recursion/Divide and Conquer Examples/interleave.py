def interleave(list1, list2):

    assert(len(list1) == len(list2))

    if len(list1) == 0:
        return []
    elif len(list1) == 1:
        return list1[0], list2[0]
    else:
        mid = len(list1) // 2
        return (interleave(list1[:mid], list2[:mid]) +
                interleave(list1[mid:], list2[mid:]))

print(interleave([], []))
print(interleave([1], [2]))
print(interleave([1, 2], [3, 4]))
print(interleave([1, 2, 3], [4, 5, 6]))