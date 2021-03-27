#!/bin/python3

import os


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = {}
    n_pairs = 0

    if n == 1:
        return 0

    for i in range(n):
        sock = ar[i]

        try:
            pairs[sock] += 1
        except KeyError:
            pairs[sock] = 1

        if pairs[sock] % 2 == 0:
            n_pairs += 1
            pairs[sock] = 0

    return n_pairs


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
