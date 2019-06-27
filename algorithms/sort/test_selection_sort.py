"""
Selection sort finds the smallest element in the unsorted list,
exchanging (swapping) it with the leftmost unsorted element

https://en.wikipedia.org/wiki/Selection_sort
"""
from typing import List

from algorithms import sort


def selection_sort(list: List) -> List:
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]
    return list


class TestSelectionSort(sort.SortTestBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = selection_sort
