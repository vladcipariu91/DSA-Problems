def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
recursive_binary_search(7, multiple)


def find_first(target, source):
    index = recursive_binary_search(target, source)
    if index is None:
        return None

    while source[index] == target:
        if index == 0:
            return 0
        elif source[index - 1] == target:
            index -= 1
        else:
            return index


print(find_first(7, multiple))


def contains(target, source):
    index = recursive_binary_search(target, source)
    return index is not None


letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False