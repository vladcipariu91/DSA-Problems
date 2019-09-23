def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    result = []
    if num == 0 or num == 1:
        result.append("")
    else:
        last = num % 10
        partial = keypad(num // 10)

        chars = get_characters(last)
        for p in partial:
            for c in chars:
                result.append(p + c)

    return result


keypad(1)
keypad(12)