"""
In this notebook, you'll be tasked with finding the length of the Longest Palindromic Subsequence (LPS) given a
string of characters.

As an example:

    With an input string, ABBDBCACB
    The LPS is BCACB, which has length = 5

In this notebook, we'll focus on finding an optimal solution to the LPS task, using dynamic programming.
There will be some similarities to the Longest Common Subsequence (LCS) task, which is outlined in detail
in a previous notebook.
"""
import pprint

pp = pprint.PrettyPrinter()


def lps(input_string):
    L = [[0 for _ in range(len(input_string))] for _ in range(len(input_string))]
    n = len(input_string)

    for i in range(n):
        L[i][i] = 1

    for s_size in range(2, n + 1):
        for start_idx in range(n - s_size + 1):
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]:
                # general match case
                L[start_idx][end_idx] = L[start_idx + 1][end_idx - 1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx - 1], L[start_idx + 1][end_idx])

    pp.pprint(L)
    return L[0][-1]


# print(lps("TACOCAT"))
# print(lps("ABBDBCACB"))
print(lps("BANANO"))
