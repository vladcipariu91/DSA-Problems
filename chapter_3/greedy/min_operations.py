def min_operations(target):
    op_count = 0

    while target != 0:
        if target % 2 == 0:
            target = target // 2
        else:
            target -= 1

        op_count += 1

    return op_count


print(min_operations(18))
