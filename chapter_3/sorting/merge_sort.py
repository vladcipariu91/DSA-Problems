def mergesort(items):
    if len(items) <= 1:
        return items

    midpoint = len(items) // 2
    left = items[:midpoint]
    right = items[midpoint:]

    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        merged += left[left_index:]

    if right_index < len(right):
        merged += right[right_index:]

    return merged


merged = merge([1, 3, 7], [2, 5, 6])
print(merged)

test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
test_list_4 = [3, 1, 2, 4]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))
print('{} to {}'.format(test_list_4, mergesort(test_list_4)))
