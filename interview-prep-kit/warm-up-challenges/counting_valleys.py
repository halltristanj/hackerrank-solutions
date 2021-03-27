#!/bin/python3

import os

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    # find and print the number of valleys walked through
    n_valleys = 0
    hike = 0
    mapping = {"D": -1, "U": 1}
    in_valley = False
    for i in range(steps):
        hike += mapping[path[i]]
        if not in_valley:
            if hike < 0:
                in_valley = True
                n_valleys += 1
        if hike >= 0:
            in_valley = False

    return n_valleys


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + "\n")

    fptr.close()
