import pytest
from solutions import find_duplicates


def test_basic_case():
    assert sorted(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1])) == [2, 3]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4, 5]) == []


def test_single_element():
    assert find_duplicates([1]) == []


def test_single_duplicate():
    assert find_duplicates([1, 1]) == [1]


def test_multiple_duplicates():
    assert sorted(find_duplicates([1, 2, 3, 4, 4, 3, 2, 1])) == [1, 2, 3, 4]


def test_large_input():
    input_data = [i for i in range(1, 100001)] + [99999, 100000]
    assert sorted(find_duplicates(input_data)) == [99999, 100000]


def test_duplicate_at_start_and_end():
    assert find_duplicates([1, 3, 2, 1]) == [1]
