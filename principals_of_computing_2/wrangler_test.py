import math
import pytest, unittest
from mock import Mock
from wrangler import remove_duplicates, intersect, merge, merge_sort

class TestWrangler(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.sorted_list1 = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 7, 10]
        self.sorted_list2 = [1, 2, 3, 3, 4, 6, 8, 8, 10]

    def test_remove_duplicates(self):
        # given
        list1_dedupped = [1, 2, 3, 4, 5, 6, 7, 10]
        list2_dedupped = [1, 2, 3, 4, 6, 8, 10]

        # when
        result1 = remove_duplicates(self.sorted_list1)
        result2 = remove_duplicates(self.sorted_list2)

        # then
        assert result1 == list1_dedupped
        assert result2 == list2_dedupped

    def test_intersect(self):
        # given
        expected = [1, 2, 3, 4, 6, 10]

        # when
        result = intersect(self.sorted_list1, self.sorted_list2)

        # then
        assert result == expected

    def test_merge(self):
        # given
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 10]

        # when
        result = merge(self.sorted_list1, self.sorted_list2)

        # then
        assert result == expected

    def test_merge_sort(self):
        # given
        to_merge_sort = [1, 9, 9, 5, 7, 7, 4, 5, 2, 3, 4, 8, 6, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # when
        result = merge_sort(to_merge_sort)

        # then
        assert result == expected
