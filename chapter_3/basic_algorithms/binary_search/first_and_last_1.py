def first_and_last_index(arr, number):
    first = first_binary_search(arr, number, 0, len(arr) - 1)
    last = last_binary_search(arr, number, 0, len(arr) - 1)

    if first is None:
        first = -1

    if last is None:
        last = -1

    return [first, last]


def first_binary_search(arr, target, start, end):
    if start > end:
        return None

    middle = (start + end) // 2

    if arr[middle] == target:
        # TODO: binary search in the first half to check if there's another one
        index = first_binary_search(arr, target, 0, middle - 1)
        if index is None:
            return middle
        else:
            return index
    elif arr[middle] < target:
        return first_binary_search(arr, target, middle + 1, end)
    else:
        return first_binary_search(arr, target, 0, middle - 1)


def last_binary_search(arr, target, start, end):
    if start > end:
        return None

    middle = (start + end) // 2

    if arr[middle] == target:
        # TODO: binary search in the second half to check if there's another one
        index = last_binary_search(arr, target, middle + 1, end)
        if index is None:
            return middle
        else:
            return index
    elif arr[middle] < target:
        return last_binary_search(arr, target, middle + 1, end)
    else:
        return last_binary_search(arr, target, 0, middle - 1)


arr = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7]
print("First: {}".format(first_binary_search(arr, 2, 0, len(arr) - 1)))
print("Last: {}".format(last_binary_search(arr, 3, 0, len(arr) - 1)))
arr = [3, 3, 3, 3, 3, 3, 3, 3, 3]
print("First: {}".format(first_binary_search(arr, 3, 0, len(arr) - 1)))
print("Last: {}".format(last_binary_search(arr, 3, 0, len(arr) - 1)))
