# In information theory, the Hamming distance between two strings of equal length is the number of positions at which
# the corresponding symbols are different. Calculate the Hamming distace for the following test cases.


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return None

    distance = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance


print("Pass" if (10 == hamming_distance('ACTTGACCGGG', 'GATCCGGTACA')) else "Fail")
print("Pass" if (1 == hamming_distance('shove', 'stove')) else "Fail")
print("Pass" if (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print("Pass" if (9 == hamming_distance('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if (2 == hamming_distance('0101010100011101', '0101010100010001')) else "Fail")
