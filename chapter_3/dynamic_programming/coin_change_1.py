"""
# Solution One

# Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
# Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1

# Base Cases:
    # when Amount == 0: F(Amount) = 0
    # when Amount < 0: F(Amount) =  float('inf')
"""


def change_coins(coins, amount):
    memo = {}

    def return_change(remaining):
        if remaining < 0:
            return float('inf')
        if remaining == 0:
            return 0

        if remaining not in memo:
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)

        return memo[remaining]

    res = return_change(amount)

    return -1 if res == float('inf') else res


print(change_coins([1, 2, 5], 11))
print(change_coins([1, 4, 5, 6], 23))
print(change_coins([5, 7, 8], 2))
