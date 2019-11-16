"""
Given a string consisting of uppercase and lowercase ASCII characters, write a function, case_sort,
that sorts uppercase and lowercase letters separately, such that if the 𝑖th place in the original string had an
uppercase character then it should not have a lowercase character after being sorted and vice versa.

For example:
Input: fedRTSersUXJ
Output: deeJRSfrsTUX
"""


def case_sort(string):
    sorted_string = case_sort_helper(string)
    upper_case_index = 0
    lower_case_index = find_lower_case_index(sorted_string)

    result = []
    for char in string:
        ascii_int = ord(char)
        if 97 <= ascii_int <= 122:
            result.append(sorted_string[lower_case_index])
            lower_case_index += 1
        else:
            result.append(sorted_string[upper_case_index])
            upper_case_index += 1

    return "".join(result)


def find_lower_case_index(sorted_string):
    for index, character in enumerate(sorted_string):
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:
            return index

    return 0


def case_sort_helper(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]

    left = case_sort_helper(left)
    right = case_sort_helper(right)

    return merge(left, right)


def merge(left, right):
    left_index = 0
    right_index = 0
    merged = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


print(case_sort("fedRTSersUXJ"))
print(case_sort("defRTSersUXI"))
print(case_sort("akghahfhgabh"))
print(case_sort("DFGJDFKGJDLKGN"))
