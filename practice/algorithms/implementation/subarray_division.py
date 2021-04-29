def birthday(s, d, m):
    """
    s: array
    d: birth day
    m: birth month
    """
    count = 0
    len_s = len(s)
    for i in range(len_s):
        summ = 0
        if i + m > len_s:
            continue

        for j in range(i, i + m):
            summ += s[j]

        if summ == d:
            count += 1

    return count
