import os
from itertools import zip_longest
from string import ascii_lowercase


# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):

    collection_1 = dict()
    collection_2 = dict()
    for i, j in zip_longest(s1, s2):
        collection_1[i] = collection_1.get(i, 0) + 1
        collection_2[j] = collection_2.get(j, 0) + 1

    count = 0
    for s in ascii_lowercase:
        val_1 = collection_1.get(s, 0)
        val_2 = collection_2.get(s, 0)
        count += max(val_1, val_2) - min(val_1, val_2)

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + "\n")

    fptr.close()
