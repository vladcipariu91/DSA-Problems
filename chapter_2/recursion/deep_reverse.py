def deep_reverse(arr):
    return deep_reverse_func(arr, 0)


def deep_reverse_func(arr, index):
    if index == len(arr):
        return []

    output = deep_reverse_func(arr, index + 1)

    if isinstance(arr[index], list):
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]

    output.append(to_append)

    return output


print(deep_reverse([1, [1, 2], 2, 3]))
