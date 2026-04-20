"""
This function takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns None. The function iterates through each string in the list, comparing their lengths to find the longest one. It initializes an empty string `longest_str` to keep track of the longest string found so far. If it finds a string that is longer than the current longest string, it updates `longest_str` with that string. Finally, it returns the longest string found in the list.
"""

def find_longest_string(strList):

    if not strList:
        return None
    
    longest_str = ""

    for string in strList:
        if len(string) > len(longest_str):
            longest_str = string

    return longest_str

# Usage of the function
string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""