import os


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    cost = 0
    count = 0
    for p in prices:
        cost += p
        count += 1
        if cost > k:
            n_toys = count - 1
            return n_toys


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + "\n")

    fptr.close()
