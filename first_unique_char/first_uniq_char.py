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
