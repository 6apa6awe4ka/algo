def ckn(values: list, k):
    n = len(values)
    ii = [i for i in range(0, k - 1)]

    while True:
        vv = [
            values[ii[i]] for i in range(0, k - 1)
        ]

        for v in values[ii[k - 2] + 1:]:
            res = vv.copy()
            res.append(v)
            yield res

        i0 = k - 2

        while i0 >= 0:
            if ii[i0] > n - k + i0:
                i0 -= 1
                continue
            break

        if i0 < 0:
            break

        index = ii[i0]
        for i1 in range(i0, k - 1):
            index += 1
            ii[i1] = index


if __name__ == '__main__':
    for v in ckn([0, 1, 2, 3, 4], 3):
        print(v)

    for v in ckn([0, 1, 2, 3], 2):
        print(v)
