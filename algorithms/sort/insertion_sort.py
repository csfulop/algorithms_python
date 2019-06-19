"""
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

https://www.geeksforgeeks.org/insertion-sort/
"""
from timeit import timeit
from typing import List
from unittest import TestCase

from hamcrest import greater_than
from hamcrest.core import assert_that
from hamcrest.core.core import is_


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


class Base:
    class InsertionSortBase(TestCase):
        def setUp(self) -> None:
            self.sort = None

        def test_sort_empty_list(self):
            assert_that(self.sort([]), is_([]))

        def test_insertion_sort(self):
            assert_that(self.sort([1]), is_([1]))
            assert_that(self.sort([1, 2]), is_([1, 2]))
            assert_that(self.sort([2, 1]), is_([1, 2]))
            assert_that(self.sort([1, 2, 3, 4, 5]), is_([1, 2, 3, 4, 5]))
            assert_that(self.sort([5, 4, 3, 2, 1]), is_([1, 2, 3, 4, 5]))
            assert_that(self.sort([1, 2, 5, 4, 3]), is_([1, 2, 3, 4, 5]))
            assert_that(self.sort(list(reversed(range(1000)))), is_(list(range(1000))))


class TestInsertionSort(Base.InsertionSortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = insertion_sort


class TestInsertionSort2(Base.InsertionSortBase):
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
