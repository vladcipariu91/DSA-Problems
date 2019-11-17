"""
input unsorted arr and integer k, 0 <= k <= n - 1
output kth smallest of arr
"""


def fast_select(arr, k):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]

    list_of_groups = break_into_groups(arr)
    median_set = set()
    for group in list_of_groups:
        group.sort()
        group_median = group[len(group) // 2]
        median_set.add(group_median)

    pivot = fast_select(list(median_set), len(median_set) // 2)
    # print("pivot is {}".format(pivot))

    smaller = []
    equal = []
    greater = []
    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)

    # print("smaller {} equal {} greater {}".format(smaller, equal, greater))
    # print("k is: {}".format(k))
    if k < len(smaller):
        return fast_select(smaller, k)
    elif k >= len(smaller) + len(equal):
        return fast_select(greater, k - len(smaller) - len(equal))
    else:
        return pivot


def break_into_groups(arr):
    list_of_groups = []
    index = 0
    group = []
    while index < len(arr):
        if index % 5 == 0:
            group = []
            list_of_groups.append(group)

        group.append(arr[index])
        index += 1

    return list_of_groups


print("expected 2, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 0)))
print("expected 5, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 1)))
print("expected 8, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 2)))
print("expected 9, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 3)))
print("expected 11, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 4)))
print("expected 11, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 5)))
print("expected 13, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 6)))
print("expected 17, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 7)))
print("expected 20, result {}".format(fast_select([5, 2, 20, 17, 11, 13, 8, 9, 11], 8)))
