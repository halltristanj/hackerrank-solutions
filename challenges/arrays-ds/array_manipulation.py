# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # n -> length of list
    # queries -> number of times to update list
    _list = [0 for x in range(n)]
    max_val = 0
    for start, end, to_add in queries:
        _list[start - 1] += to_add
        try:
            _list[end] -= to_add
        except IndexError:
            pass

    prev = 0
    for i in range(len(_list)):
        prev += _list[i]
        _list[i] = prev
        if prev > max_val:
            max_val = prev

    return max_val


if __name__ == "__main__":
    # fptr = open('output.dat', 'w')

    # nm = input().split()
    n, m = 10000000, 100000

    queries = []

    with open("input.dat", "r") as _file:
        in_data = _file.readlines()

    for data in in_data:
        data.replace("\n", "")
        queries.append(list(map(int, data.split())))
        a = queries

    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
