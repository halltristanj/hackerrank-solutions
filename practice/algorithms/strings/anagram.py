import os


# Complete the anagram function below.
def anagram(s):
    len_s = len(s)
    if len_s % 2 != 0:
        return -1

    mid = len_s // 2
    left = s[:mid]
    right = s[mid:]
    if left == right:
        return 0

    collection = dict()
    for i, j in zip(left, right):
        collection[i] = collection.get(i, 0) + 1
        collection[j] = collection.get(j, 0) - 1

    count = 0
    for x in collection.values():
        if x > 0:
            count += x

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + "\n")

    fptr.close()
