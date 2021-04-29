def kangaroo(x1, v1, x2, v2):
    """
    It's physics.

    x_1(t) = x1 + v1 * t
    x_2(t) = x2 + v2 * t
    Solve for t.
    Since we're working with arrays, can only use integers.
    That's why compare t with t_floor.
    """
    if v2 == v1 and x1 != x2:
        return "NO"

    t = (x1 - x2) / (v2 - v1)
    t_floor = (x1 - x2) // (v2 - v1)

    if t < 0 or t != t_floor:
        return "NO"
    return "YES"
