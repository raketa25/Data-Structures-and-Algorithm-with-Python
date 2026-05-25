"""
This code defines a function `group_anagrams` that takes a list of strings as input and groups the anagrams together. An anagram is a word formed by rearranging the letters of another word. The function uses a dictionary to group the anagrams by sorting the characters of each word and using the sorted string as the key. The values in the dictionary are lists of anagrams that correspond to each key. Finally, the function returns a list of lists, where each inner list contains the anagrams grouped together. The code also includes test cases to demonstrate the expected output for different sets of input strings.
"""

def group_anagrams(strings):
    my_dict = {}
    for word in strings:
        key = " ".join(sorted(word))
        if key not in my_dict:
            my_dict[key] = []
        my_dict[key].append(word)
    anagrams_list = list(my_dict.values())
    return anagrams_list
    


# Test cases
if __name__ == "__main__":
    
    print("1st set:")
    print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

    print("\n2nd set:")
    print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

    print("\n3rd set:")
    print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



    """
        EXPECTED OUTPUT:
        ----------------
        1st set:
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

        2nd set:
        [['abc', 'cba', 'bac'], ['foo'], ['bar']]

        3rd set:
        [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

    """