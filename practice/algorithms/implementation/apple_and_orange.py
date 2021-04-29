from itertools import zip_longest


# Complete the countApplesAndOranges function below.
def count_apples_and_oranges(s, t, a, b, apples, oranges):
    """
    s: Starting of house
    t: Ending of house
    a: Where apple tree is located
    b: Where Orange tree is located
    apples: n apples
    oranges: n oranges
    """
    collection = {
        "apples": 0,
        "oranges": 0,
    }

    for apple, orange in zip_longest(apples, oranges):
        if apple:
            a_dist = apple + a
            collection["apples"] += 1 if s <= a_dist <= t else 0
        if orange:
            o_dist = orange + b
            collection["oranges"] += 1 if s <= o_dist <= t else 0

    print(collection["apples"])
    print(collection["oranges"])
