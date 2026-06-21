"""
Complete the solution so that it splits the string into strings of two characters in a list/array (depending on the language you use). If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Solution:
Down below is a Python implementation of the solution to split a string into pairs of two characters. If the string has an odd length, the last pair will have an underscore added to it.
Also included is a commented-out version using list comprehension for a more concise approach.

Finally a JavaScript implementation is provided in the comments for reference too.
"""
# ===================== Python Solution =====================
print("="*20, "SPLIT STRING", "="*20)
def solution(s):
    pairs = []
    
    for i in range(0, len(s), 2):
        pairs.append(s[i:i+2])
    
    if len(s) % 2 != 0:
        pairs[-1] += '_'
    
    return pairs

# Using list comprehension
# def solution(s):
#     new_s = [s[i:i+2] for i in range(0, len(s), 2)]

#     if len(s) % 2 != 0:
#         new_s[-1] = new_s[-1] + '_'

#     return new_s

# Test cases:
if __name__ == "__main__":
    print(solution("abcdef"))  # Output: ['ab', 'cd', 'ef']
    print(solution("abcde"))   # Output: ['ab', 'cd', 'e_']
    print(solution(""))         # Output: []
    print(solution("a"))        # Output: ['a_']
    print(solution("ab"))       # Output: ['ab']
    print(solution("abc"))      # Output: ['ab', 'c_']



# JavaScript: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/javascript
# function solution(s) {
#     const pairs = [];
    
#     for (let i = 0; i < s.length; i += 2) {
#         pairs.push(s.slice(i, i + 2));
#     }
    
#     if (s.length % 2 !== 0) {
#         pairs[pairs.length - 1] += '_';
#     }
    
#     return pairs;
# }