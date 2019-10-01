def diagonal_difference(arr):
    # Write your code here
    primary = 0
    secondary = 0
    arr_len = len(arr)
    for i in range(arr_len):
        primary += arr[i][i]
        print("secondary diagonal {}: ".format(arr[arr_len - i - 1][i]))
        secondary += arr[arr_len - i - 1][i]

    return abs(primary - secondary)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

diagonal_difference(arr)
