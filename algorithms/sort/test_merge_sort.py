"""
Merge Sort is a Divide and Conquer algorithm.
It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

https://www.geeksforgeeks.org/merge-sort/
"""
from typing import List

from  algorithms import sort


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


class TestMergeSort(sort.SortBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = merge_sort
