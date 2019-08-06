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
    heap = Heap()
    for item in input:
        heap.add(item)
    result = list()
    while len(heap) > 0:
        result.append(heap.pop())
    return list(reversed(result))  # FIXME: use min heap and remove reversed


class TestHeapSort(sort.SortTestBase):
    def setUp(self) -> None:
        super().setUp()
        self.sort = heap_sort
