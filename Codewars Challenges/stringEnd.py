"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Solution:
The function `solution` checks if the string `s` ends with the substring `end`.
It does this by comparing the last characters of `s` with `end`. If they match, it returns `True`; otherwise, it returns `False`.
The second implementation achieves the same result by slicing the string `s` from the end, using the length of `end` to determine how many characters to compare.
"""

# def solution(s, end):
#     if s.endswith(end):
#         return True
#     else:
#         return False

# Compact version using the built-in `endswith` method
# def solution(s, end):
#     return s.endswith(end)

# Secondsoluion
def solution(s, end):
    if s[-len(end):] == end:
        return True
    else:
        return False

# Compact version using slicing
# def solution(s, end):
#     return s[-len(end):] == end

# Test cases:
if __name__ == "__main__":
    print(solution("abc", "bc"))  # Output: True
    print(solution("abc", "d"))   # Output: False
    print(solution("abc", "abc")) # Output: True
    print(solution("abc", ""))    # Output: True
    print(solution("", ""))       # Output: True
    print(solution("abc", "abcd")) # Output: False