#!/bin/python3

import os

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    string_count = dict()
    query_count = []

    # Gives us the n occurrences of a given string in `strings`.
    for string in strings:
        try:
            string_count[string] += 1
        except KeyError:
            string_count[string] = 1

    for query in queries:
        query_count.append(string_count.get(query, 0))

    return query_count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
