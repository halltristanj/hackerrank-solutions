def divisible_sum_pairs(n, k, ar):
    """
    n: the length of ar
    ar: the array
    k: integer to check
    """
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count
