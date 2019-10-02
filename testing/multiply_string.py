a = "b"
b = 3 * a
print(b)


def flippingBits(n):
    str = 32 * "1"
    return int(str, 2) - n


print(flippingBits(9))
