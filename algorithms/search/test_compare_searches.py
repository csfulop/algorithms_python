from timeit import timeit
from unittest import TestCase

from algorithms.search import _test_search_with_big_data
from algorithms.search.test_binary_search import binary_search
from algorithms.search.test_linear_search import linear_search


class TestCompareSearches(TestCase):
    def test_compare_searches(self):
        searches = (linear_search, binary_search)
        for search in searches:
            f = lambda: _test_search_with_big_data(search, items=100000, positive_tests=10, negative_tests=10)
            time = timeit(f, number=1)
            print(search.__name__, time)
