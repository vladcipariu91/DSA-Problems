def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)


def first_and_last_index(arr, number):
    index = recursive_binary_search(number, arr)
    if index is None:
        return [-1, -1]

    first = find_first(arr, number, index)
    last = find_last(arr, number, index)

    return [first, last]


def find_first(arr, number, index):
    while arr[index] == number:
        if index == 0:
            return 0
        elif arr[index - 1] == number:
            index -= 1
        else:
            return index


def find_last(arr, number, index):
    while arr[index] == number:
        if index == len(arr) - 1:
            return index
        elif arr[index + 1] == number:
            index += 1
        else:
            return index


input_list = [1]
print(first_and_last_index(input_list, 1))  # [0, 0]

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
print(first_and_last_index(input_list, 3))  # [3, 6]

input_list = [0, 1, 2, 3, 4, 5]
print(first_and_last_index(input_list, 5))  # [5, 5]
print(first_and_last_index(input_list, 6))  # [-1, -1]

