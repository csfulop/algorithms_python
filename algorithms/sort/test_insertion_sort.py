"""
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

https://www.geeksforgeeks.org/insertion-sort/
"""
from timeit import timeit
from typing import List
from unittest import TestCase

from hamcrest import greater_than
from hamcrest.core import assert_that

from algorithms import sort


def insertion_sort(list: List) -> List:
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j - 1], list[j] = list[j], list[j - 1]
            else:
                break
    return list


def insertion_sort2(list: List) -> List:
    for i in range(1, len(list)):
        x = list[i]
        for j in range(i - 1, -1, -1):
            if list[j] > x:
                list[j + 1] = list[j]
            else:
                list[j + 1] = x
                break
        else:
            list[0] = x
    return list


class TestInsertionSort(sort.SortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = insertion_sort


class TestInsertionSort2(sort.SortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = insertion_sort2


class CompareInsertionSortSpeeds(TestCase):
    def test_optimized_should_be_faster(self):
        input = list(reversed(range(1000)))
        t1 = timeit(lambda: insertion_sort(input), number=1)
        print(t1)
        input = list(reversed(range(1000)))
        t2 = timeit(lambda: insertion_sort2(input), number=1)
        print(t2)
        assert_that(t1, greater_than(t2))
