#!/bin/python3

import os

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)]
    last_answer = 0
    answers = []

    for query_list in queries:
        query, x, y = query_list
        idx = (x ^ last_answer) % n

        if query == 1:
            arr[idx].append(y)

        elif query == 2:
            list_in_arr = arr[idx]
            element_idx = y % len(list_in_arr)
            last_answer = list_in_arr[element_idx]
            answers.append(last_answer)

    return answers


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(f"result: {result}")
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
