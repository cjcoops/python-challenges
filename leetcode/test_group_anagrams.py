from solutions import group_anagrams


def test_basic_case():
    assert sorted(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == sorted(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )


def test_empty_string():
    assert group_anagrams(["", ""]) == [["", ""]]


def test_single_characters():
    assert sorted(group_anagrams(["a", "b", "c", "a"])) == sorted(
        [["a", "a"], ["b"], ["c"]]
    )


def test_no_anagrams():
    assert sorted(group_anagrams(["cat", "dog", "bird"])) == [
        ["bird"],
        ["cat"],
        ["dog"],
    ]


def test_large_input():
    input_data = ["abc"] * 1000 + ["def"] * 1000
    output = group_anagrams(input_data)
    assert len(output) == 2
    assert sorted(output[0]) == ["abc"] * 1000
    assert sorted(output[1]) == ["def"] * 1000


def test_mixed_case():
    assert sorted(group_anagrams(["abc", "bca", "cab", "def", "fed"])) == sorted(
        [["abc", "bca", "cab"], ["def", "fed"]]
    )
