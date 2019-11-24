"""
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers.
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ
by more than 1.
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.
"""


def rearrange_digits(input_list):
    sorted_list = sort_descending(input_list)
    if len(sorted_list) <= 1:
        return None
    if len(sorted_list) == 2:
        return input_list

    first = ""
    i = 0
    while i < len(sorted_list):
        first += str(sorted_list[i])
        i += 2

    second = ""
    i = 1
    while i < len(sorted_list):
        second += str(sorted_list[i])
        i += 2

    return [int(first), int(second)]


def sort_descending(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2

    left = input_list[:mid]
    right = input_list[mid:]

    left = sort_descending(left)
    right = sort_descending(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
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


print(rearrange_digits([1, 2, 3, 4, 5]))
# expected [531, 42]
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# expected [964, 852]
print(rearrange_digits([1, 1, 1, 1]))
# expected [11, 11]
print(rearrange_digits([0]))
# expected None
print(rearrange_digits([]))
# expected None
print(rearrange_digits([1, 9, 1, 9]))
# expected [91, 91]
print(rearrange_digits([0, 0, 0, 0]))
# expected [0, 0]
print(rearrange_digits([0, 1, 0, 0]))
# expected [10, 0]
print(rearrange_digits([1, 2, 3, 0]))
# expected [31, 20]
