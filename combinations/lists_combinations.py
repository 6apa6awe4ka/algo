def combinations(lists):
    n = len(lists)
    lii = [len(l) - 1 for l in lists[:n - 1]]
    ii = [0 for i in range(0, n - 1)]

    while True:
        vv = [lists[i][ii[i]] for i in range(0, n - 1)]
        for v in lists[n - 1]:
            res = vv.copy()
            res.append(v)
            yield res

        i = n - 2

        while i >= 0:
            if ii[i] >= lii[i]:
                ii[i] = 0
                i -= 1
                continue
            break

        if i < 0:
            break

        ii[i] += 1


if __name__ == '__main__':
    lists = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    for v in combinations(lists):
        print(v)
