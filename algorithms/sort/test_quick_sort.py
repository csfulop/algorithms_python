"""
QuickSort is a Divide and Conquer algorithm.
It picks an element as pivot and partitions the given array around the picked pivot.

https://www.geeksforgeeks.org/quick-sort/
"""
from typing import List

from algorithms import sort


def quick_sort(list: List, low=0, high=None) -> List:
    def _swap(i, j):
        if i != j:
            list[i], list[j] = list[j], list[i]

    def _partition():
        i = low - 1
        pivot = list[high]
        for j in range(low, high):
            if list[j] < pivot:
                i += 1
                _swap(i, j)
        _swap(i + 1, high)
        return i + 1

    if high is None:
        high = len(list) - 1
    if low < high:
        partition_index = _partition()
        quick_sort(list, low, partition_index - 1)
        quick_sort(list, partition_index + 1, high)
    return list


class TestQuickSort(sort.SortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = quick_sort
