"""
Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps.
In how many possible ways can you climb the staircase if the staircase has n steps?
Write a recursive function to solve the problem.

Example:

    n = 3
    output = 4

The output is 4 because there are four ways we can climb the staircase:

1. 1 step +  1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
4. 3 steps
"""


def staircase(n):
    print("step: {} ".format(n))
    if n <= 0:
        return 1

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


print(staircase(7))
