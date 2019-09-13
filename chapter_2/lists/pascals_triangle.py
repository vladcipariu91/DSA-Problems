def nth_row_pascal(n):
    current_row = [1]
    if n == 0:
        return current_row

    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]

        for j in range(1, i):
            next_val = previous_row[j - 1] + previous_row[j]
            current_row.append(next_val)

        current_row.append(1)

    return current_row


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)

n = 7
solution = [1, 7, 21, 35, 35, 21, 7, 1]

test_case = [n, solution]
test_function(test_case)

print(nth_row_pascal(100))
