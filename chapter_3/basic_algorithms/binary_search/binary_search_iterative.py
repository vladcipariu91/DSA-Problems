def binary_search(array, target):
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1

    return -1


print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
