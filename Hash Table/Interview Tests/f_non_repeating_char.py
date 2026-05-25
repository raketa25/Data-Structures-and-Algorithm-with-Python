"""
This code defines a function `first_non_repeating_char` that takes a string as input and returns the first non-repeating character in the string. The function uses a dictionary to count the occurrences of each character in the string. It then iterates through the string again to find and return the first character that has a count of 1. If there are no non-repeating characters, it returns `None`. The code also includes test cases to demonstrate the expected output for different input strings.
"""

def first_non_repeating_char(string):
    my_dict = {}
    # char_list = list(string)
    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1
        
    for char in string:
        if my_dict[char] == 1:
            return char
            
    return None



# Test cases
if __name__ == "__main__":
    
    print( first_non_repeating_char('leetcode') )

    print( first_non_repeating_char('hello') )

    print( first_non_repeating_char('aabbcc') )



    """
        EXPECTED OUTPUT:
        ----------------
        l
        h
        None

    """