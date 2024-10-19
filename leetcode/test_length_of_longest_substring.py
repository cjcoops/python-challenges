# Tests for length_of_longest_substring module

from solutions import length_of_longest_substring


def test_example1():
    assert length_of_longest_substring("abcabcbb") == 3


def test_example2():
    assert length_of_longest_substring("bbbbb") == 1


def test_example3():
    assert length_of_longest_substring("pwwkew") == 3


def test_empty_string():
    assert length_of_longest_substring("") == 0


def test_single_character():
    assert length_of_longest_substring("a") == 1


def test_no_repeating_characters():
    assert length_of_longest_substring("abcdefg") == 7


def test_longer_string_with_repeats():
    assert length_of_longest_substring("abcabcde") == 5


def test_string_with_spaces():
    assert length_of_longest_substring("a b c a b c") == 3


def test_string_with_special_characters():
    assert length_of_longest_substring("!@#$%^&*()") == 10


def test_string_with_digits():
    assert length_of_longest_substring("1234567890") == 10


def test_mixed_characters():
    assert length_of_longest_substring("abc123!@#") == 9


def test_multiple_repeats():
    assert length_of_longest_substring("abcdeabcde") == 5  # "abcde"
