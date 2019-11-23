"""
Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
"""
import random


def get_min_max(ints):
    if len(ints) == 0:
        return None, None
    elif len(ints) == 1:
        return ints[0], ints[0]
    else:
        if ints[0] > ints[1]:
            maximum = ints[0]
            minimum = ints[1]
        else:
            maximum = ints[1]
            minimum = ints[0]

    for i in range(2, len(ints)):
        if ints[i] > maximum:
            maximum = ints[i]
        if ints[i] < minimum:
            minimum = ints[i]

    return minimum, maximum


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
l1 = [100, 23, -100, 32, 1000, 99, 999, 232]

print(get_min_max(l))
# expected (0, 9)
print(get_min_max(l1))
# expected (-100, 1000)
print(get_min_max([]))
# expected (None, None)
print(get_min_max([1]))
# expected (1, 1)
