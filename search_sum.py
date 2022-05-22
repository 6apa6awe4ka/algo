# Надо бы проверить полным перебором
# Реализовать Ckn
from collections import defaultdict


def search_sum(values: list, n: int, n_sum: int):
    if n == 1:
        return n_sum in set(values)
    elif n == 2:
        for i1, v1 in enumerate(values[:-1]):
            for v2 in values[i1 + 1:]:
                v = v1 + v2
                if v == n_sum:
                    return True
    elif n == 3:
        for i1, v1 in enumerate(values):
            for i2, v2 in enumerate(values[i1 + 1:], start=i1 + 1):
                for v3 in values[i2 + 1:]:
                    v = v1 + v2 + v3
                    if v == n_sum:
                        return True
    elif n == 4:
        for i1, v1 in enumerate(values):
            for i2, v2 in enumerate(values[i1 + 1:], start=i1 + 1):
                for i3, v3 in enumerate(values[i2 + 1:], start=i2 + 1):
                    for v4 in values[i3 + 1:]:
                        v = v1 + v2 + v3 + v4
                        if v == n_sum:
                            return True
    else:
        n_bits = [int(v) for v in reversed(bin(n)[2:])]
        b_sum = defaultdict(list)
        for i, v in enumerate(values):
            b_sum[v].append({i})

        sum_sets = [b_sum] if n_bits[0] else []

        for b in n_bits[1:-1]:
            res = defaultdict(list)
            for v, i in merge_gen(b_sum, b_sum):
                res[v] += i
            if b:
                sum_sets.append(res)
            b_sum = res

        if n_bits.index(1) == len(n_bits) - 1:
            for v1, i1 in merge_gen(b_sum, b_sum):
                if v1 == n_sum:
                    return True
        else:
            result_set = sum_sets[0]

            for sum_set in sum_sets[1:]:
                res = defaultdict(list)
                for v, i in merge_gen(result_set, sum_set):
                    res[v] += i
                result_set = res

            for v1, i1 in merge_gen(b_sum, b_sum):
                v2 = n_sum - v1
                if v2 in result_set:
                    i2 = result_set[v2]
                    for i1i in i1:
                        for i2i in i2:
                            if not (i1i & i2i):
                                return True
    return False


def merge_gen(set1, set2):
    result_set = {}
    for v1, i1 in set1.items():
        for v2, i2 in set2.items():
            v = v1 + v2
            ii = [] if v not in result_set else result_set[v]

            for i1i in i1:
                for i2i in i2:
                    if i1i & i2i:
                        continue
                    i = i1i.union(i2i)
                    ii.append(i)
            if ii:
                yield v, ii


if __name__ == '__main__':
    values_for_test = [2, 3, 4, 6, 7, 12]

    values = values_for_test + [i for i in range(max(values_for_test), 10)]
    n = len(values_for_test)
    n_sum = sum(values_for_test)

    assert search_sum(values, n, n_sum) is True

    values = [i for i in range(0, 100)]
    n = 2
    n_sum = 198

    assert search_sum(values, n, n_sum) is False

    values = [1, 2, 3, 7]
    n = 3
    n_sum = 9

    assert search_sum(values, n, n_sum) is False

    values = [1, 7, 2, 3, 7]
    n = 2
    n_sum = 14
    assert search_sum(values, n, n_sum) is True


    values = [0, 7, 1, 11, 2, 3, 14]
    n = 4
    n_sum = 6
    assert search_sum(values, n, n_sum) is True

    values = [6, 1, 8]
    n = 3
    n_sum = 22
    assert search_sum(values, n, n_sum) is False

    values = [0, 1, 0, 1]
    n = 4
    n_sum = 2
    assert search_sum(values, n, n_sum) is True

    values = [-7, 2, -2, 3, -6, 2, 8, -3]
    n = 4
    n_sum = 11
    assert search_sum(values, n, n_sum) is True
