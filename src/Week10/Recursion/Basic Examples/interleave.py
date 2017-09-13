def interleave(list1, list2):
    assert(len(list1) == len(list2))

    if len(list1) == 0:
        return []
    else:
        return [list1[0], list2[0]] + interleave(list1[1:], list2[1:])

print(interleave([1,2,3],[4,5,6]))  # [1,4,2,5,3,6]