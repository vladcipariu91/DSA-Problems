a = "b"
b = 3 * a


def nonDivisibleSubset(k, s):
    arr = list(s)
    l_arr = len(arr)
    subset = set()
    for i in range(0, l_arr - 1):
        for j in range(i + 1, l_arr):
            if (arr[i] + arr[j]) % k == 0:
                subset.add(arr[i])
                subset.add(arr[j])




nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436])
