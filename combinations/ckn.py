# дополнительно: написать рекурсивно
def ckn(values: list, k):
    n = len(values)
    ii = [i for i in range(0, k - 1)]

    while ii[0] <= n - k:
        # собираем вектор согласно текущим индексам k - 1 векторов
        vv = [
            values[ii[i]] for i in range(0, k - 1)
        ]
        # перебираем последний элемент вектора и передаем его далее из генератора
        for v in values[ii[k - 2] + 1:]:
            res = vv.copy()
            res.append(v)
            yield res

        # устанавливаем новые индексы для k - 1 векторов
        for i in range(k - 2, -1, -1):
            if ii[i] <= n - k + i:
                index = ii[i]
                for i0 in range(i, k - 1):
                    index += 1
                    ii[i0] = index
                break


if __name__ == '__main__':
    for v in ckn([0, 1, 2, 3], 3):
        print(v)

    for v in ckn([0, 1, 2, 3], 2):
        print(v)
