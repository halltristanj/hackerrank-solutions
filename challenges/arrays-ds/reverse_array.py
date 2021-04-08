#!/bin/python3

import os

# Complete the reverseArray function below.
def reverseArray(a):
    # return a[::-1]
    # or
    start = 0
    end = len(a) - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return a


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(" ".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
