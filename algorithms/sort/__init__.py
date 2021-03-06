from unittest import TestCase

from hamcrest.core import assert_that
from hamcrest.core.core import is_


class SortTestBase(TestCase):
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
        assert_that(self.sort(list(reversed(range(100)))), is_(list(range(100))))
        assert_that(self.sort(list(reversed(range(101)))), is_(list(range(101))))

    def test_sort_list_with_same_items(self):
        assert_that(self.sort([1, 2, 1]), is_([1, 1, 2]))
        assert_that(
            self.sort(list(reversed(range(100))) + list(range(100))),
            is_([x for y in range(100) for x in (y, y)]))
