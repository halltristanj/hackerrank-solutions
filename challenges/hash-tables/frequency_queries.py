import os


# Complete the freqQuery function below.
def freqQuery(queries):
    collection = dict()
    count_collection = dict()
    solution = []
    for operation, value in queries:
        if operation == 1:  # Insert
            # Store that we've seen this value
            prev_count = collection.get(value, 0)
            collection[value] = prev_count + 1
            new_count = collection.get(value)

            count_collection[new_count] = count_collection.get(new_count, 0) + 1

            count_collection[prev_count] = max(
                0, count_collection.get(prev_count, 0) - 1
            )
            if count_collection[prev_count] <= 0:
                del count_collection[prev_count]

        if operation == 2:  # Remove
            prev_count = collection.get(value, 0)
            collection[value] = max(0, prev_count - 1)
            new_count = collection.get(value)

            count_collection[prev_count] = max(
                0, count_collection.get(prev_count, 0) - 1
            )
            count_collection[new_count] = count_collection.get(new_count, 0) + 1

            if count_collection[new_count] <= 0:
                del count_collection[new_count]

            if collection[value] <= 0:
                del collection[value]

        if operation == 3:  # Record
            result = 1 if count_collection.get(value, 0) > 0 else 0
            solution.append(result)

    return solution


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write("\n".join(map(str, ans)))
    fptr.write("\n")

    fptr.close()
