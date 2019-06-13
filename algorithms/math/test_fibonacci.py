import time
from functools import wraps


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_iter(n):
    def f(a, b, count):
        if count == 0:
            return a
        else:
            return f(b, a + b, count - 1)

    return f(0, 1, n)


def fib_iter_2(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fib_iter_2(n - 1, b, a + b)


def fib_iter_3(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def memo(f):
    cache = {}

    @wraps(f)
    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return wrapper


@memo
def fib_memo(n):
    if n <= 1:
        return n
    else:
        return fib_memo(n - 1) + fib_memo(n - 2)


# FIXME: add O(log n) algorithm

def _test_basic(fib):
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21


def _test_speed(fib, n):
    t1 = time.time()
    result = fib(n)
    t2 = time.time()
    print('%s(%d)=%d' % (fib.__name__, n, result))
    run_time = t2 - t1
    print('  run time=%f' % run_time)
    return run_time


def test_fib():
    _test_basic(fib)


def test_fib_iter():
    _test_basic(fib_iter)


def test_fib_iter_2():
    _test_basic(fib_iter_2)


def test_fib_iter_3():
    _test_basic(fib_iter_3)


def test_fib_memo():
    _test_basic(fib_memo)


def test_speed():
    run_time_fib = _test_speed(fib, 20)
    run_time_fib_iter = _test_speed(fib_iter, 20)
    run_time_fib_memo = _test_speed(fib_memo, 20)
    assert run_time_fib_iter < run_time_fib
    assert run_time_fib_memo < run_time_fib
    _test_speed(fib_memo, 40)
    _test_speed(fib_memo, 80)
    _test_speed(fib_memo, 160)
