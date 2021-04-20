import os
from itertools import zip_longest


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    collection = dict()
    for i, j in zip_longest(a, b):
        collection[i] = collection.get(i, 0) + 1
        collection[j] = collection.get(j, 0) - 1

    count = 0
    for letter, _sum in collection.items():
        if letter is not None and _sum != 0:
            count += abs(_sum)

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + "\n")

    fptr.close()
