def merge_sort(values):
    n = len(values)
    size = 2

    while True:
        buf = []
        tail = n % step

        i1 = 0
        i2 = size

        while i2 < n:
            i1_next = i2 + size
            for ii in range(0, size * 2):
                v1 = values[i1]
                v2 = values[i2]
                if i2 == i1_next or v1 > v2:
                    i1 += 1
                    buf.append(v1)
                else:
                    i2 += 1
                    buf.append(v2)
            i1 = i1_next
            i2 = i1 + size

        if tail > size:


        size *= 2
        values = buf
