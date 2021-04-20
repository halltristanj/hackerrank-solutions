# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # This is wrong.... got to go through the whole array and see if
    # any expenditure is > median of past d days.
    len_exp = len(expenditure)
    if d > len_exp:
        return 0

    # print(f'd: {d}')
    # print(f'expends: {expenditure}')
    # print(f'len exp: {len_exp}')

    left = (d - 1) // 2
    right = -(-(d - 1) // 2)
    # print(left, right)

    # Counting sort array. Initialize 201 elements 0 -> 200 (inclusive).
    # 200 is a boundary condition.
    count_sort = [0] * 201
    for i in range(d):
        count_sort[expenditure[i]] += 1

    count = 0
    i = d
    while i < len_exp:
        # print(f'count sort 1: {count_sort}')
        # print(f'expenditure[{i}]: {expenditure[i]}')

        j = 0
        k = 0
        while k <= left:
            # print(k)
            k += count_sort[j]
            j += 1
        m1 = j - 1
        # print(f'm1: {m1}')
        k = 0
        j = 0
        while k <= right:
            k += count_sort[j]
            j += 1
        m2 = j - 1
        # print(f'm2: {m2}')
        median = (m1 + m2) / 2

        if int(expenditure[i]) >= 2 * median:
            # print(f'{expenditure[i]} > {2 * median}')
            count += 1

        count_sort[expenditure[i - d]] -= 1
        count_sort[expenditure[i]] += 1

        # print(f'count sort 2: {count_sort}')

        i += 1

    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])

    # d = int(nd[1])

    d = 10000

    # expenditure = list(map(int, input().rstrip().split()))

    with open("input.dat", "r") as _file:
        expenditure = _file.readlines()

    expenditure = [int(x) for x in expenditure[0].split()]
    # expenditure = expenditure[0].split()

    # d = 5
    # expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

    result = activityNotifications(expenditure, d)

    print(result)
    answer = 633
    if result != answer:
        raise AssertionError(f"no equal {answer}: {result}")

    # fptr.write(str(result) + '\n')

    # fptr.close()
