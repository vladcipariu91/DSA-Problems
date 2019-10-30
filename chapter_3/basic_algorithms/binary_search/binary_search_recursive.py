def binary_search(array, target, start_index, end_index):
    middle_index = (start_index + end_index) // 2

    if start_index > end_index:
        return -1

    if array[middle_index] == target:
        return middle_index
    elif array[middle_index] < target:
        return binary_search(array, target, middle_index + 1, end_index)
    else:
        return binary_search(array, target, 0, middle_index - 1)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 1, 0, len(arr) - 1))
print(binary_search(arr, 2, 0, len(arr) - 1))
print(binary_search(arr, 3, 0, len(arr) - 1))
print(binary_search(arr, 4, 0, len(arr) - 1))
print(binary_search(arr, 5, 0, len(arr) - 1))
print(binary_search(arr, 6, 0, len(arr) - 1))
print(binary_search(arr, 7, 0, len(arr) - 1))
print(binary_search(arr, 8, 0, len(arr) - 1))
print(binary_search(arr, 9, 0, len(arr) - 1))
print(binary_search(arr, 10, 0, len(arr) - 1))
print(binary_search(arr, 0, 0, len(arr) - 1))
