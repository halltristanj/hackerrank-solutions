import os


# Complete the gameOfThrones function below.
def gameOfThrones(s):
    collection = dict()
    for i in s:
        collection[i] = collection.get(i, 0) + 1

    n_odds = 0
    n_evens = 0
    for value in collection.values():
        if value % 2 != 0:
            n_odds += 1
            if n_odds > 1:
                return "NO"
        else:
            n_evens += 1

    if n_evens > 0:
        return "YES"

    return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + "\n")

    fptr.close()
