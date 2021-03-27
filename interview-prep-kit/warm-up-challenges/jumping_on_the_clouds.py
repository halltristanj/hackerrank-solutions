#!/bin/python3

import os


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # Determine the minimum number of jumps it
    #  will take to jump from the starting postion to the last cloud
    # Beginning and end are always 0

    if len(c) == 2:
        return 1

    i = 0
    jumps = 0
    while i < len(c):
        if i < len(c) - 1:
            one_ahead = c[i + 1]
        if i < len(c) - 2:
            two_ahead = c[i + 2]

        if not two_ahead:
            i += 2
            jumps += 1
        elif not one_ahead:
            i += 1
            jumps += 1
        else:
            i += 1

        if i == len(c) - 1:
            break

    return jumps


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + "\n")

    fptr.close()
