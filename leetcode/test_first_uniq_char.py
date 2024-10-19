from solutions import first_uniq_char


def test_example1():
    assert first_uniq_char("leetcode") == 0


def test_example2():
    assert first_uniq_char("loveleetcode") == 2


def test_no_unique_char():
    assert first_uniq_char("aabbcc") == -1


def test_empty_string():
    assert first_uniq_char("") == -1


def test_single_char():
    assert first_uniq_char("z") == 0
