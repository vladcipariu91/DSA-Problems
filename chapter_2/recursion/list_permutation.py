import copy


def permute(l):
    perm = []
    if len(l) == 0:
        perm.append([])
    else:
        first_element = l[0]
        sub_permutes = permute(l[slice(1, None)])

        for p in sub_permutes:
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(j, first_element)
                perm.append(r)

    return perm


permute([1, 2, 3])
