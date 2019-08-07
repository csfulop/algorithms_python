from typing import List

from algorithms import sort
from algorithms.data_structure.test_heap import Heap


def heap_sort(input: List) -> List:
    """
    Heap sort is a comparison based sorting technique based on Binary Heap data structure.
    https://www.geeksforgeeks.org/heap-sort/
    :param input: list to be sorted
    :return: the sorted list
    """
    heap = Heap(items=input, comparator=int.__lt__)
    result = list()
    while len(heap) > 0:
        result.append(heap.pop())
    return result


class TestHeapSort(sort.SortTestBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = heap_sort
