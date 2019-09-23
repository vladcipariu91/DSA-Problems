"""
Given an array arr and a target element target, find the last index of occurrence of target in arr using recursion.
If target is not present in arr, return -1.

For example:

    For arr = [1, 2, 5, 5, 4] and target = 5, output = 3

    For arr = [1, 2, 5, 5, 4] and target = 7, output = -1

"""


def last_index_of(arr, target):
    return last_index_of_func(arr, target, len(arr) - 1)


def last_index_of_func(arr, target, index):
    if index < 0:
        return -1

    if arr[index] == target:
        return index

    return last_index_of_func(arr, target, index - 1)


def last_ind(arr, target):
    result = -1
    for index, it in enumerate(arr):
        if it == target:
            result = index

    return result


print(last_index_of([1, 2, 3, 5, 5, 6], 5))
print(last_index_of([1, 2, 3, 5, 5, 6], 7))
