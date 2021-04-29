def migratory_birds(arr):
    collection = dict()
    max_amount = 0
    max_collection = dict()  # Collection of values at the maximum amount
    for a in arr:
        collection[a] = collection.get(a, 0) + 1
        if collection[a] >= max_amount:
            max_amount = collection[a]
            if max_amount not in max_collection.keys():
                max_collection[max_amount] = [a]
            else:
                max_collection[max_amount].append(a)

    lowest_of_most = min(max_collection[max_amount])
    return lowest_of_most
