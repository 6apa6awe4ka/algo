# need tests
def merge_sort(values: list):
    start = 0
    end = len(values)
    buf = values.copy()
    split(values, buf, start, end)


def split(values, buf, start, end):
    if start - end <= 1:
        return
    bottom = (start + end) // 2
    split(buf, values, start, bottom)
    split(buf, values, bottom, end)
    merge(buf, values, start, bottom, end)


def merge(values, buf, start, bottom, end):
    for i in range(start, end):
        if bottom == end or values[start] > values[bottom]:
            buf[i] = values[start]
            start += 1
        else:
            buf[i] = values[bottom]
            bottom += 1


def merge_sort_non_recursive(values):
    n = len(values)
    buf = [None for i in range(0, n)]
    size = 1

    while True:
        start = 0

        while True:
            bottom = start + size
            end = bottom + size
            if end >= n:
                break
            merge(values, buf, start, bottom, end)
            start = end

        if bottom >= n:
            for i in range(start, n):
                buf[i] = values[i]
        else:
            merge(values, buf, start, bottom, n)

        size *= 2

        if size >= n:
            return buf

        values, buf = buf, values
