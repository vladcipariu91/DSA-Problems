for i in range(1, 10):
    for j in range(1, 10):
        print("i: {} j: {}".format(i, j))
        if j == 3:
            print("continue")
            continue

a_set = set()
a_set.add(1)

print(a_set)

a_map = {"a": 1}
if "a" in a_map:
    del a_map["a"]
if "a" in a_map:
    del a_map["a"]
print(a_map)
