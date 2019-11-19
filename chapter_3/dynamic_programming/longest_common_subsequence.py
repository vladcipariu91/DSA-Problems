def lcs(string_a, string_b):
    if len(string_a) >= len(string_b):
        max_str = string_a
        min_str = string_b
    else:
        max_str = string_b
        min_str = string_a
    mat = [[0 for _ in range(len(max_str) + 1)] for _ in range(len(min_str) + 1)]

    line = 0
    while line < len(min_str):
        b = min_str[line]
        col = 0
        while col < len(max_str):
            a = max_str[col]
            if a == b:
                mat[line + 1][col + 1] = 1 + max(mat[line][col + 1], mat[line + 1][col])
            else:
                mat[line + 1][col + 1] = max(mat[line][col + 1], mat[line + 1][col])
            col += 1

        line += 1
        print(mat)

    return mat[-1][-1]


print(lcs('ABCD', 'BD'))

"""
    Start with a matrix that has one extra row and column of zeros.
    As you traverse your string:
        - If there is a match, fill that grid cell with the value to the top-left of that cell plus one. So, in our case, 
        when we found a matching B-B, we added +1 to the value in the top-left of the matching cell, 0.
        - If there is not a match, take the maximum value from either directly to the left or the top cell, and carry that 
        value over to the non-match cell.
"""
