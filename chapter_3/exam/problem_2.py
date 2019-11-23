"""
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order
of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""


def rotated_array_search(input_list, number):
    """
        Find the index by searching in a rotated sorted array

        Args:
           input_list(array), number(int): Input array to search and the target
        Returns:
           int: Index or -1
        """
    return search(input_list, number, 0, len(input_list) - 1)


def search(a, t, s, e):
    m = (s + e) // 2

    if s > e:
        return -1

    mid = a[m]
    if mid == t:
        return m
    else:
        is_left_sorted = a[s] < a[m - 1]
        is_right_sorted = a[m + 1] < a[e]
        if is_left_sorted:
            if a[s] <= t <= a[m - 1]:
                return search(a, t, s, m - 1)
            else:
                return search(a, t, m + 1, e)
        elif is_right_sorted:
            if a[m + 1] <= t <= a[e]:
                return search(a, t, m + 1, e)
            else:
                return search(a, t, s, m - 1)
        else:
            if a[m - 1] == t:
                return m - 1
            elif a[m + 1] == t:
                return m + 1
            else:
                return -1


print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 4))
# expected 8
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 0))
# expected 2
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 7))
# expected 1
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 8))
# expected -1
print(rotated_array_search([], 8))
# expected -1

print("for 0")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 0))
# expected 0
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 0))
# expected 6
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 0))
# expected 5
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 0))
# expected 4
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 0))
# expected 3
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 0))
# expected 2
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 0))
# expected 1

print("for 1")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 1))
# expected 1
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 1))
# expected 0
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 1))
# expected 6
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 1))
# expected 5
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 1))
# expected 4
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 1))
# expected 3
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 1))
# expected 2

print("for 2")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 2))
# expected 2
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 2))
# expected 1
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 2))
# expected 0
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 2))
# expected 6
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 2))
# expected 5
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 2))
# expected 4
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 2))
# expected 3

print("for 3")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 3))
# expected -1
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 3))
# expected -1
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 3))
# expected -1
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 3))
# expected -1
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 3))
# expected -1
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 3))
# expected -1
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 3))
# expected -1

print("for 4")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 4))
# expected 3
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 4))
# expected 2
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 4))
# expected 1
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 4))
# expected 0
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 4))
# expected 6
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 4))
# expected 5
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 4))
# expected 4

print("for 5")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 5))
# expected 4
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 5))
# expected 3
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 5))
# expected 2
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 5))
# expected 1
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 5))
# expected 0
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 5))
# expected 6
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 5))
# expected 5

print("for 6")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 6))
# expected 5
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 6))
# expected 4
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 6))
# expected 3
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 6))
# expected 2
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 6))
# expected 1
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 6))
# expected 0
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 6))
# expected 6

print("for 7")
print(rotated_array_search([0, 1, 2, 4, 5, 6, 7], 7))
# expected 6
print(rotated_array_search([1, 2, 4, 5, 6, 7, 0], 7))
# expected 5
print(rotated_array_search([2, 4, 5, 6, 7, 0, 1], 7))
# expected 4
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 7))
# expected 3
print(rotated_array_search([5, 6, 7, 0, 1, 2, 4], 7))
# expected 2
print(rotated_array_search([6, 7, 0, 1, 2, 4, 5], 7))
# expected 1
print(rotated_array_search([7, 0, 1, 2, 4, 5, 6], 7))
# expected 0
