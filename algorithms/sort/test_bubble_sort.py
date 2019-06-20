"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

https://www.geeksforgeeks.org/bubble-sort/
"""
from timeit import timeit
from typing import List

from hamcrest import less_than
from hamcrest.core import assert_that

from algorithms import sort


def bubble_sort(list: List) -> List:
    """
    Bubble sort the given list
    :param list: list to be sorted
    :return: the sorted list
    """
    for i in range(len(list) - 1, 0, -1):
        sorted = True
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                sorted = False
        if sorted:
            break
    return list


class TestBubbleSort(sort.SortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = bubble_sort

    def test_optimized_bubble_sort(self):
        sorted_list = list(range(1000))
        t1 = timeit(lambda: bubble_sort(sorted_list), number=1)
        print(t1)
        reversed_list = list(reversed(range(1000)))
        t2 = timeit(lambda: bubble_sort(reversed_list), number=1)
        print(t2)
        assert_that(t1 * 3, less_than(t2))
