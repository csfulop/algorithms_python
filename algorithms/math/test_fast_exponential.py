def fast_exp(x, n):
    if n < 0:
        raise Exception()
    if n == 0:
        return 1
    elif n % 2:
        return x * fast_exp(x, n - 1)
    else:
        y = fast_exp(x, n // 2)
        return y * y


def test():
    assert fast_exp(2, 0) == 1
    assert fast_exp(2, 1) == 2
    assert fast_exp(2, 2) == 4
    assert fast_exp(2, 3) == 8
    assert fast_exp(2, 20) == 2 ** 20
