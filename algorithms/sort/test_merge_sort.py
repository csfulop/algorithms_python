"""
Merge Sort is a Divide and Conquer algorithm.
It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

https://www.geeksforgeeks.org/merge-sort/
"""
from timeit import timeit
from typing import List
from unittest import TestCase

from hamcrest import greater_than
from hamcrest.core import assert_that

from algorithms import sort


def merge_sort(list: List) -> List:
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    first_half = merge_sort(list[:middle])
    second_half = merge_sort(list[middle:])

    result = []
    while first_half and second_half:
        if first_half[0] < second_half[0]:
            result.append(first_half.pop(0))
        else:
            result.append(second_half.pop(0))
    if first_half:
        result.extend(first_half)
    if second_half:
        result.extend(second_half)

    return result


def merge_sort2(list: List) -> List:
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    first_half = merge_sort(list[:middle])
    second_half = merge_sort(list[middle:])

    i, j, k = 0, 0, 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            list[k] = first_half[i]
            i += 1
            k += 1
        else:
            list[k] = second_half[j]
            j += 1
            k += 1
    while i < len(first_half):
        list[k] = first_half[i]
        i += 1
        k += 1
    while j < len(second_half):
        list[k] = second_half[j]
        j += 1
        k += 1

    return list


class TestMergeSort(sort.SortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = merge_sort


class TestMergeSort2(sort.SortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = merge_sort2


class CompareMergeSortSpeeds(TestCase):
    def test_merge_short_without_pop0_should_be_faster(self):
        input = list(reversed(range(50000)))
        t1 = timeit(lambda: merge_sort(input), number=1)
        print(t1)
        input = list(reversed(range(50000)))
        t2 = timeit(lambda: merge_sort2(input), number=1)
        print(t2)
        assert_that(t1, greater_than(t2))
