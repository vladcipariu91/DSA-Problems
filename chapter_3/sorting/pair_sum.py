from quicksort import quicksort


def pair_sum(arr, target):
    quicksort(arr)
    start_index = 0
    end_index = len(arr) - 1

    while start_index < end_index:
        sum = arr[start_index] + arr[end_index]
        if sum == target:
            return arr[start_index], arr[end_index]
        elif sum < target:
            start_index += 1
        else:
            end_index -= 1

    return None, None


input_list = [2, 7, 11, 15]
target = 9
print(pair_sum(input_list, target))

input_list = [0, 8, 5, 7, 9]
target = 9
print(pair_sum(input_list, target))

input_list = [110, 9, 89]
target = 9
print(pair_sum(input_list, target))