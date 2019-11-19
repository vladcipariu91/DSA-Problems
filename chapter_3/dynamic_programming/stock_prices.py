"""
You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock
price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a function
that returns the maximum profit obtainable. You will need to buy before you can sell.

For example, suppose you have the following prices:

prices = [3, 4, 7, 8, 6]

    Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have 13
    elements (one price for each 30 minute interval betwen 9:30 and 4:00), as seen in the test cases further down in
    this notebook.

In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell at a price of 8 to
yield a maximum profit of 5. In other words, you are looking for the greatest possible difference between two numbers
in the array.
"""


def max_returns(prices):
    if len(prices) < 2:
        return

    min_index = 0
    max_index = 1
    current_min_index = 0

    for index in range(1, len(prices)):
        if prices[index] < prices[current_min_index]:
            current_min_index = index

        print("current min index: {}".format(current_min_index))

        if prices[index] - prices[current_min_index] > prices[max_index] - prices[min_index]:
            min_index = current_min_index
            max_index = index

        print("min index {}\nmax index {}".format(min_index, max_index))

    return 0 if prices[max_index] < prices[min_index] else prices[max_index] - prices[min_index]


print(max_returns([3, 4, 7, 8, 6]))
print(max_returns([2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]))
print(max_returns([54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]))
print(max_returns([78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]))
