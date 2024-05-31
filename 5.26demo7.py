def max(x, y):
    return x if x > y else y


def maxs(a, b, c, d):
    res1 = max(a, b)
    res2 = max(res1, c)
    res3 = max(res2, d)
    return res3


print(maxs(5, 2, 420, 299))

