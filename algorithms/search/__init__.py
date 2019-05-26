from random import randint
from timeit import timeit
from typing import Callable

from hamcrest.core import assert_that
from hamcrest.core.core import is_


def _test_search_with_big_data(search: Callable, items=100000, positive_tests=10, negative_tests=10):
    list = _generate_test_list(items)

    def test():
        for i in range(positive_tests):
            pos = randint(0, len(list) - 1)
            result = search(list, list[pos])
            assert_that(result, is_(pos))
        for i in range(negative_tests):
            pos = randint(0, len(list) - 1)
            try:
                search(list, list[pos] + 1)
            except ValueError:
                continue
            raise Exception('ValueError was not raised')

    time = timeit(test, number=1)
    return time


def _generate_test_list(items):
    list = [randint(2, 3)]
    for i in range(items):
        list.append(list[-1] + randint(2, 3))
    return list
