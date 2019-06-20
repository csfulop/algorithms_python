from unittest import TestCase

from hamcrest.core import assert_that
from hamcrest.core.core import is_


class SortBase(TestCase):
    def setUp(self) -> None:
        self.sort = None

    def test_sort_empty_list(self):
        assert_that(self.sort([]), is_([]))

    def test_basic_sort(self):
        assert_that(self.sort([1]), is_([1]))
        assert_that(self.sort([1, 2]), is_([1, 2]))
        assert_that(self.sort([2, 1]), is_([1, 2]))
        assert_that(self.sort([1, 2, 3, 4, 5]), is_([1, 2, 3, 4, 5]))
        assert_that(self.sort([5, 4, 3, 2, 1]), is_([1, 2, 3, 4, 5]))
        assert_that(self.sort([1, 2, 5, 4, 3]), is_([1, 2, 3, 4, 5]))
        assert_that(self.sort(list(reversed(range(1000)))), is_(list(range(1000))))
