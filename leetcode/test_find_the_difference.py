from solutions import (
    find_the_difference,
)  # Replace 'your_module' with the actual module name where the function is located


def test_example1():
    assert find_the_difference("abcd", "abcde") == "e"


def test_example2():
    assert find_the_difference("", "y") == "y"


def test_single_extra_letter():
    assert find_the_difference("a", "aa") == "a"


def test_large_case():
    s = "x" * 9999
    t = "x" * 10000
    assert find_the_difference(s, t) == "x"


def test_shuffled_characters():
    assert find_the_difference("abcd", "bacde") == "e"


def test_repeated_letters():
    assert find_the_difference("aabbcc", "aabbccd") == "d"


def test_same_letters_different_order():
    assert find_the_difference("xyz", "yzxw") == "w"


def test_all_same_letter():
    assert find_the_difference("pppp", "ppppp") == "p"


def test_multiple_occurrences():
    assert find_the_difference("aabb", "aabbb") == "b"
