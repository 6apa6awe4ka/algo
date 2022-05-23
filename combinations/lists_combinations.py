def combinations(lists):
    n = len(lists)
    lii = [len(l) - 1 for l in lists[1:]]
    ii = [0 for i in range(0, n - 1)]

    while True:
        vv = [lists[i][ii[i]] for i in range(0, n - 1)]
        for v in lists[0]:
            res = vv.copy()
            res.append(v)
            yield res

        for i in range(n - 2, -1, -1):
            if ii[i] < lii[i]:
                ii[i] += 1
                break
            ii[i] = 0

        if i == 0 and ii[i] == 0:
            break


if __name__ == '__main__':
    lists = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    for v in combinations(lists):
        print(v)