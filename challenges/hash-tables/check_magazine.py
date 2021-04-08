from collections import defaultdict
from itertools import zip_longest


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    ransom = defaultdict(lambda: 0)
    for m, n in zip_longest(magazine, note):
        ransom[n] += 1
        ransom[m] -= 1
    for n in note:
        if ransom[n] is None:
            continue
        if ransom[n] > 0:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
