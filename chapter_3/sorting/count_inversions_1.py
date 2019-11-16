def counting_inversions(arr):
    result = mergesort(arr)
    return result[1]


def mergesort(items):
    if len(items) <= 1:
        return items, 0

    midpoint = len(items) // 2
    left = items[:midpoint]
    right = items[midpoint:]

    left = mergesort(left)
    right = mergesort(right)
    output = left[1] + right[1]
    result = merge(left[0], right[0])
    output += result[1]
    return result[0], output


def merge(left, right):
    merged = []
    inv_count = 0
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            inv_count += len(left) - left_index
            merged.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        merged += left[left_index:]

    if right_index < len(right):
        merged += right[right_index:]

    return merged, inv_count


# merged = merge([1, 3, 7], [2, 5, 6])
# print(merged)

test_list_1 = [0, 1]
test_list_2 = [2, 1]
test_list_3 = [2, 5, 1, 3, 4]
test_list_4 = [3, 1, 2, 4]
test_list_5 = [7, 5, 3, 8]
test_list_6 = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
test_list_7 = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
print(counting_inversions(test_list_4))
print(counting_inversions(test_list_5))
print(counting_inversions(test_list_1))
print(counting_inversions(test_list_2))
print(counting_inversions(test_list_3))
print(counting_inversions(test_list_6))
print(counting_inversions(test_list_7))
