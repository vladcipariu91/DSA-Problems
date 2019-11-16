def sort_a_little_bit(items, start_index, end_index):
    left_index = start_index
    # choose the last element as the pivot
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while pivot_index != left_index:
        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        # Place the item before the pivot at left_index
        items[left_index] = items[pivot_index - 1]
        # Shift pivot one to the left
        items[pivot_index - 1] = pivot_value
        # Place item at pivot's previous location
        items[pivot_index] = item
        # Update pivot index
        pivot_index -= 1

    return pivot_index


def sort_all(items, start_index, end_index):
    if end_index <= start_index:
        return

    pivot_index = sort_a_little_bit(items, start_index, end_index)
    sort_all(items, start_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items) - 1)


items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
