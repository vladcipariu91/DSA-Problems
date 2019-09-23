def permute(l):
    perm = []
    if len(l) == 0:
        perm.append("")
    else:
        first_element = l[0]
        sub_permutes = permute(l[slice(1, None)])

        for p in sub_permutes:
            for j in range(0, len(p) + 1):
                if j == 0:
                    r = first_element + p
                elif j == len(p):
                    r = p + first_element
                else:
                    r = p[0:j] + first_element + p[j:]

                perm.append(r)

    return perm


print(permute("abc"))
