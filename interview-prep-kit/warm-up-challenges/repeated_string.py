#!/bin/python3

import os


# Complete the repeatedString function below.
def repeatedString(s, n):

    # Go through string 1x to count the number of `a`s.
    if n < len(s):
        return sum([1 for i in range(n) if s[i] == "a"])

    number_of_a = sum([1 for x in s if x == "a"])

    len_s = len(s)
    n_segments = n // len_s
    remainder = n % len_s

    # Multiply number of `a`s found by segments
    count = number_of_a * n_segments

    # Then run through remainder
    count += sum([1 for x in range(remainder) if s[x] == "a"])

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + "\n")

    fptr.close()
