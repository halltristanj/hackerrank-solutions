import os

# from collections import Counter

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    # Write your code here
    # x = Counter(candles)
    # return x[max(x)]
    # or
    collection = dict()
    _max = 0
    for c in candles:
        collection[c] = collection.get(c, 0) + 1
        if collection[c] > _max:
            _max = collection[c]

    return _max


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + "\n")

    fptr.close()
