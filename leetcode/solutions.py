from collections import Counter, defaultdict

# Simple solution:
# sorting is O(n log n) for each string
# comparing sorted string is O(n)
# def is_anagram(s, t):
#     return "".join(sorted(s)) == "".join(sorted(t))


# Optimal solution - O(n)
def is_anagram(s, t):
    return Counter(s) == Counter(t)


# Simple solution using .count()
# O(n^2) complexity since outer loop can run n times and string.count(char) runs over the entire string

# def first_uniq_char(string: str) -> int:

#     for index, char in enumerate(string):
#         if string.count(char) == 1:
#             return index

#     return -1


# Optimized solution is O(n), we make 2 passes over the string 1 to build the counts, 1 to find the first unique character
def first_uniq_char(string: str) -> int:
    counts = {}

    for char in string:
        counts[char] = counts.get(char, 0) + 1

    for index, char in enumerate(string):
        if counts[char] == 1:
            return index

    return -1


# Solution has O(n) time complexity since both pointers only move forward
def length_of_longest_substring(s):
    char_set = set()  # To track characters in the current window
    left = 0  # Left pointer for the sliding window
    max_length = 0  # Variable to store the maximum length found

    for right in range(len(s)):  # Right pointer for the sliding window
        # If the character is already in the set, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1  # Move the left pointer to the right

        char_set.add(s[right])  # Add the current character to the set
        max_length = max(max_length, right - left + 1)  # Update max_length

    return max_length


def find_the_difference(a, b):
    difference = Counter(b) - Counter(a)
    return next(iter(difference))


# O(n * k log k) where n is number of words, k is average length of each word
# Loop through n words
# Sorting each words is O(k log k)
def group_anagrams(anagrams):
    groups = defaultdict(list)

    for string in anagrams:
        sorted_string = "".join(sorted(string))

        groups[sorted_string].append(string)

    return list(groups.values())


# Time complexity O(n) as we only iterate through array once
# Space complexity O(1) extra space
# Since all elements are [1..n], can use the value of each element to index directly into array (subtracting 1 to keep in range)
def find_duplicates(nums):
    result = []

    # Iterate over each number in the array
    for i in range(len(nums)):
        # Get the index corresponding to the current number
        index = abs(nums[i]) - 1

        # If the number at nums[index] is already negative, we found a duplicate
        if nums[index] < 0:
            result.append(abs(nums[i]))
        else:
            # Mark the number as seen by making the value at the corresponding index negative
            nums[index] = -nums[index]

    return result
