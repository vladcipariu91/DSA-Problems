"""
Given an input_list and a target, return the indices of pair of integers in the list that sum to the target.
The best solution takes O(n) time. You can assume that the list does not have any duplicates.

For e.g. input_list = [1, 5, 9, 7, 3] and target = 8, the answer would be [0, 3]
"""


def pair_sum_to_target(input_list, target):
    index_dict = dict()
    result = []
    for index, element in enumerate(input_list):
        if target - element in index_dict:
            result.append([index_dict[target - element], index])
        index_dict[element] = index

    return result


print(pair_sum_to_target([1, 5, 9, 7, 3], 8))
