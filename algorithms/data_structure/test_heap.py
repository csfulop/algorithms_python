from copy import deepcopy
from unittest import TestCase

from hamcrest import is_
from hamcrest.core import assert_that


class Heap:
    def __init__(self, items=None):
        self._data = [] if items is None else deepcopy(items)
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._heapify_down(i)
        # FIXME: use comparator to be able to create min/max heap

    def size(self) -> int:
        return len(self._data)

    def __len__(self):
        return self.size()

    def __getitem__(self, item):
        return self._data[item]

    def add(self, item) -> None:
        self._data.append(item)
        self._heapify_up()

    def pop(self):
        result = self._data[0]
        self._data[0] = self._data[-1]
        del self._data[-1]
        self._heapify_down(0)
        return result

    def _heapify_up(self, index=None):
        if index is None:
            index = len(self._data) - 1
        if index > 0:
            parent = (index - 1) // 2
            if index < len(self) and self[index] > self[parent]:
                self._data[parent], self._data[index] = self[index], self[parent]
                self._heapify_up(parent)

    def _heapify_down(self, index=0):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if left < len(self) and self[left] > self[index]:
            largest = left
        if right < len(self) and self[right] > self[largest]:
            largest = right
        if largest != index:
            self._data[largest], self._data[index] = self[index], self[largest]
            self._heapify_down(largest)


class TestHeap(TestCase):
    def test_size_of_empty_heap(self):
        heap = Heap()
        assert_that(heap.size(), is_(0))
        assert_that(len(heap), is_(0))

    def test_add_item(self):
        self._assert_heap_add([10], [10])
        self._assert_heap_add([10, 9], [10, 9])
        self._assert_heap_add([9, 10], [10, 9])
        self._assert_heap_add([10, 9, 8], [10, 9, 8])
        self._assert_heap_add([8, 9, 10], [10, 8, 9])
        self._assert_heap_add([10, 9, 8, 7], [10, 9, 8, 7])
        self._assert_heap_add([7, 8, 9, 10], [10, 9, 8, 7])
        self._assert_heap_add([7, 8, 9, 10, 11], [11, 10, 8, 7, 9])

    def _assert_heap_add(self, input, expected):
        assert_that(self._build_heap(input)._data, is_(expected))

    def _build_heap(self, input):
        heap = Heap()
        for item in input:
            heap.add(item)
        return heap

    def test_getitem(self):
        heap = self._build_heap([3, 2, 1])
        self.assertRaises(TypeError, lambda: heap['asdf'])
        assert_that(heap[0], is_(3))
        assert_that(heap[1], is_(2))
        assert_that(heap[2], is_(1))
        assert_that(heap[-1], is_(1))

    def test_pop_item(self):
        self._assert_heap_pop([5, 4, 2, 3, 1], [4, 3, 2, 1])
        self._assert_heap_pop([7, 5, 6, 4, 3, 2, 1], [6, 5, 2, 4, 3, 1])

    def _assert_heap_pop(self, heap_data, expedted_after_pop):
        heap = Heap()
        heap._data = deepcopy(heap_data)
        max_item = heap.pop()
        assert_that(heap._data, is_(expedted_after_pop))
        assert_that(max_item, is_(heap_data[0]))

    def test_build_heap_from_list(self):
        heap = Heap([1, 2, 3, 4, 5])
        assert_that(heap._data, is_([5, 4, 3, 1, 2]))
