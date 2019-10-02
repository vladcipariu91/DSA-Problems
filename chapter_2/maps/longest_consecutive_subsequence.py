"""
Given list of integers that contain numbers in random order, write a program to find the longest possible
sub sequence of consecutive numbers in the array. Return this subsequence in sorted order.
The solution must take O(n) time

For e.g. given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5

Note- If two arrays are of equal length return the array whose index of smallest element comes first.
"""


def longest_consecutive_subsequence(input_list):
    element_dict = dict()

    for index, element in enumerate(input_list):
        element_dict[element] = index

    max_length = -1
    starts_at = len(input_list)

    for index, element in enumerate(input_list):
        current_starts = index
        element_dict[element] = -1

        current_count = 1

        # check upwards
        current = element + 1

        while current in element_dict and element_dict[current] > 0:
            current_count += 1
            element_dict[current] = -1
            current = current + 1

        # check downwards
        current = element - 1
        while current in element_dict and element_dict[current] > 0:
            current_starts = element_dict[current]
            current_count += 1
            element_dict[current] = -1
            current = current - 1

        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            max_length = current_count

    start_element = input_list[starts_at]

    return [element for element in range(start_element, start_element + max_length)]


print(longest_consecutive_subsequence([2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6]))
