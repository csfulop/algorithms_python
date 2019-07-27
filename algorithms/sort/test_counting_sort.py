"""
Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values.
Then doing some arithmetic to calculate the position of each object in the output sequence.

https://www.geeksforgeeks.org/counting-sort/
"""
from typing import List

from algorithms import sort


def counting_sort(list: List, max=101) -> List:
    """alternative (maybe bit more pythonic) implementation of counting sort using result.append()"""
    counts = [0] * max
    for i in list:
        counts[i] += 1
    result = []
    for i in range(max):
        c = counts[i]
        while c > 0:
            result.append(i)
            c -= 1
    return result


def counting_sort_2(list: List, max=101) -> List:
    """Counting sort as originally described: transforming counts to indexes"""
    counts = [0] * max
    for i in list:
        counts[i] += 1
    for i in range(1, max):
        counts[i] += counts[i - 1]
    result = [None] * len(list)
    for i in range(len(list)):
        result[counts[list[i]] - 1] = list[i]
        counts[list[i]] -= 1
    return result


class TestCountingSort(sort.SortTestBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = counting_sort


class TestCountingSort2(sort.SortTestBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = counting_sort_2
