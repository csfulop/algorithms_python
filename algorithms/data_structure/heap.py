from unittest import TestCase

from hamcrest import is_
from hamcrest.core import assert_that


class Heap:
    def __init__(self):
        self._data = []

    def size(self) -> int:
        return len(self._data)

    def __len__(self):
        return self.size()

    def add(self, item: int) -> None:
        self._data.append(item)
        self._heapify_up()

    def _heapify_up(self, index=None):
        if index is None:
            index = len(self._data) - 1
        if index > 0:
            parent = (index - 1) // 2
            if self._heapify_child(parent, index):
                self._heapify_up(parent)

    def _heapify_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        self._heapify_child(index, left) or self._heapify_child(index, right)
        # FIXME: recursion

    def _heapify_child(self, index, child):
        if child < len(self._data) and self._data[child] > self._data[index]:
            self._data[child], self._data[index] = self._data[index], self._data[child]
            return True
        return False


class TestHeap(TestCase):
    def test_size_of_empty_heap(self):
        heap = Heap()
        assert_that(heap.size(), is_(0))
        assert_that(len(heap), is_(0))

    def test_add_item(self):
        self._assert_heap_build([10], [10])
        self._assert_heap_build([10, 9], [10, 9])
        self._assert_heap_build([9, 10], [10, 9])
        self._assert_heap_build([10, 9, 8], [10, 9, 8])
        self._assert_heap_build([8, 9, 10], [10, 8, 9])
        self._assert_heap_build([10, 9, 8, 7], [10, 9, 8, 7])
        self._assert_heap_build([7, 8, 9, 10], [10, 9, 8, 7])
        self._assert_heap_build([7, 8, 9, 10, 11], [11, 10, 8, 7, 9])

    def _assert_heap_build(self, input, expected):
        heap = Heap()
        for item in input:
            heap.add(item)
        assert_that(heap._data, is_(expected))
