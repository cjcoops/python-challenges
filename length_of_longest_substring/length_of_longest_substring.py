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


if __name__ == "__main__":
    length_of_longest_substring()
