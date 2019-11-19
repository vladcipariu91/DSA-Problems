import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    lookup_table = [0 for _ in range(knapsack_max_weight + 1)]

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

        print("{} {}".format(item, lookup_table))

    return lookup_table[-1]


print(max_value(6, [Item(2, 6), Item(5, 9), Item(4, 5), Item(1, 10)]))
