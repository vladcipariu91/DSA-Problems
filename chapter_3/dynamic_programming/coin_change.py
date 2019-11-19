def coin_change(coins, amount):
    min_coin = coins[0]
    if amount < min_coin:
        return -1

    max_coin = coins[-1]
    if amount % max_coin == 0:
        return amount // max_coin

    index = len(coins) - 1
    count = 0
    while amount != 0 and index >= 0:
        if amount >= coins[index]:
            count += amount // coins[index]
            amount -= count * coins[index]

        index -= 1

    return count


print(coin_change([1, 4, 5, 6], 23))
