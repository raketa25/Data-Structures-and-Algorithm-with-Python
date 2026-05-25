"""
This problem is commonly known as "Group Anagrams". The idea is to group words that are anagrams of each other together. An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.
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