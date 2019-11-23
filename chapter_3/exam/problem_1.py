"""
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
"""


def sqrt(number):
    sqrt = number / 2
    temp = 0
    while sqrt != temp:
        temp = sqrt
        sqrt = (number / temp + temp) / 2

    return int(sqrt)


print(sqrt(65))
# expected 8
print(sqrt(27))
# expected 5
print(sqrt(35))
# expected 5
print(sqrt(0))
# expected 0
print(sqrt(1000001))
# expected 1000
