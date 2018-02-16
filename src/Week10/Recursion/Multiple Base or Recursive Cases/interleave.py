def interleave(list1, list2):

    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        return [list1[0], list2[0]] + interleave(list1[1:], list2[1:])

print(interleave([], []))
print(interleave([1], [2]))
print(interleave([1], [3, 4]))
print(interleave([1, 2, 3], [4, 5, 6]))