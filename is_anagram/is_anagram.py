from collections import Counter

# Simple solution:
# sorting is O(n log n) for each string
# comparing sorted string is O(n)
# def is_anagram(s, t):
#     return "".join(sorted(s)) == "".join(sorted(t))


# Optimal solution - O(n)
def is_anagram(s, t):
    return Counter(s) == Counter(t)
