def add_one(arr):
    carry = 0
    last_elem = len(arr) - 1
    if arr[last_elem] == 9:
        arr[last_elem] = 0
        carry = 1
    else:
        arr[last_elem] += 1

    if carry == 1:
        for i in range(len(arr) - 2, -1, -1):
            if carry == 1:
                if arr[i] == 9:
                    arr[i] = 0
                    carry = 1
                else:
                    arr[i] += 1
                    carry = 0

    if carry == 1:
        arr.insert(0, 1)

    return arr


print(add_one([1, 2, 3]))
print(add_one([9, 9, 9]))
print(add_one([8, 9, 9]))
