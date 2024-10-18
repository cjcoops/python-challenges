from is_anagram import is_anagram


def test_anagram_true():
    assert is_anagram("anagram", "nagaram") == True


def test_anagram_false():
    assert is_anagram("rat", "car") == False


def test_empty_strings():
    assert is_anagram("", "") == True


def test_single_letter_same():
    assert is_anagram("a", "a") == True


def test_single_letter_different():
    assert is_anagram("a", "b") == False


def test_different_lengths():
    assert is_anagram("hello", "helloo") == False


def test_anagram_with_repeated_chars():
    assert is_anagram("aabbcc", "abcabc") == True


def test_not_anagram_with_same_characters():
    assert is_anagram("aabbcc", "abcabcx") == False


def test_large_input():
    s = "a" * 10000 + "b" * 10000 + "c" * 10000
    t = "b" * 10000 + "a" * 10000 + "c" * 10000
    assert is_anagram(s, t) == True
