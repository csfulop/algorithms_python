"""
Linear search.
"""
from typing import List
from unittest import TestCase

from hamcrest.core import assert_that
from hamcrest.core.core import is_

from algorithms.search import _test_search_with_big_data


def linear_search(list: List, element) -> int:
    """
    Using linear search to find element in list and return its position.
    :param list: list
    :param element: the item to be find
    :return: position of element in list, raise ValueError if not found
    """
    for i in range(len(list)):
        if list[i] == element:
            return i
    raise ValueError('%s not found' % str(element))


class TestLinearSearch(TestCase):
    def test_search_empty_list(self):
        with self.assertRaises(ValueError):
            linear_search([], 1)

    def test_search(self):
        assert_that(linear_search([1], 1), is_(0))
        for i in range(3):
            assert_that(linear_search([1, 2, 3], i + 1), is_(i))
        for i in range(4):
            assert_that(linear_search([1, 2, 3, 4], i + 1), is_(i))
        for i in range(5):
            assert_that(linear_search([1, 2, 3, 4, 5], i + 1), is_(i))

    def test_not_found(self):
        for i in (1, 3):
            with self.assertRaises(ValueError):
                linear_search([2], i)
        for i in (1, 3, 5):
            with self.assertRaises(ValueError):
                linear_search([2, 4], i)
        for i in (1, 3, 5, 7):
            with self.assertRaises(ValueError):
                linear_search([2, 4, 6], i)

    def test_big_data(self):
        _test_search_with_big_data(linear_search)
