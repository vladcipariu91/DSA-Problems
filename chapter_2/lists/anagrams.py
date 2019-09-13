def anagram_checker(str1, str2):
    chars_arr = initialise_char_list()

    for c in str1:
        if not is_space(c):
            chars_arr[ord(c.lower()) % 26] += 1

    for c in str2:
        if not is_space(c):
            chars_arr[ord(c.lower()) % 26] -= 1

    for i in chars_arr:
        if i != 0:
            return False

    return True


def initialise_char_list():
    arr = []

    for i in range(0, 26):
        arr.append(0)

    return arr


def is_space(char):
    return ord(char) == 32


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
