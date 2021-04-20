# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[i]}")


if __name__ == "__main__":
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
