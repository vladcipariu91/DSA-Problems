"""
Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice,
that would still be an O(n) solution but it will not count as single traversal.
"""


def sort_012(input_list):
    if input_list is None:
        return input_list

    zeros = 0
    ones = 0
    twos = 0
    for i in input_list:
        if i == 0:
            zeros += 1
        if i == 1:
            ones += 1
        if i == 2:
            twos += 1

    i = 0
    while zeros > 0:
        input_list[i] = 0
        zeros -= 1
        i += 1

    while ones > 0:
        input_list[i] = 1
        ones -= 1
        i += 1

    while twos > 0:
        input_list[i] = 2
        twos -= 1
        i += 1

    return input_list


print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
# expected [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
# expected [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
# expected [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print(sort_012([]))
# expected []
print(sort_012([0, 0, 0]))
# expected [0, 0, 0]
print(sort_012([1, 1, 1]))
# expected [1, 1, 1]
print(sort_012([2, 2, 2]))
# expected [2, 2, 2]
print(sort_012([2, 2, 1]))
# expected [1, 2, 2]
print(sort_012([2, 2, 0]))
# expected [0, 2, 2]
print(sort_012([1, 0, 0]))
# expected [0, 0, 1]
