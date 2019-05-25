"""
Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

https://www.geeksforgeeks.org/binary-search/
"""
from typing import List
from unittest import TestCase

from hamcrest.core import assert_that
from hamcrest.core.core import is_

from algorithms.search import test_search_with_big_data


def binary_search(list: List, element) -> int:
    """
    Using binary search to find element in sorted list and return its position
    :param list: sorted list
    :param element: the item to be find
    :return: position of element in list, raise ValueError if not found
    """
    if not list:
        raise ValueError('%s not found' % str(element))
    mid_pos = len(list) // 2
    mid_val = list[mid_pos]
    if mid_val == element:
        return mid_pos
    elif element < mid_val:
        return binary_search(list[0:mid_pos], element)
    else:
        return binary_search(list[mid_pos + 1:], element) + mid_pos + 1


class TestBinarySearch(TestCase):
    def test_search_empty_list(self):
        with self.assertRaises(ValueError):
            binary_search([], 1)

    def test_search(self):
        assert_that(binary_search([1], 1), is_(0))
        for i in range(3):
            assert_that(binary_search([1, 2, 3], i + 1), is_(i))
        for i in range(4):
            assert_that(binary_search([1, 2, 3, 4], i + 1), is_(i))
        for i in range(5):
            assert_that(binary_search([1, 2, 3, 4, 5], i + 1), is_(i))

    def test_not_found(self):
        for i in (1, 3):
            with self.assertRaises(ValueError):
                binary_search([2], i)
        for i in (1, 3, 5):
            with self.assertRaises(ValueError):
                binary_search([2, 4], i)
        for i in (1, 3, 5, 7):
            with self.assertRaises(ValueError):
                binary_search([2, 4, 6], i)

    def test_big_data(self):
        test_search_with_big_data(binary_search)
