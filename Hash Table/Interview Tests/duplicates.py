"""
This Code defines a function `find_duplicates` that takes a list as input and returns a list of duplicate elements found in the input list. The function uses a dictionary to count the occurrences of each element in the list. If an element appears more than once, it is added to the `dup_list`, which is returned at the end. The function also handles the case where the input list is empty or `None`. The expected output for various test cases is provided in the comments at the end of the code.
"""

def find_duplicates(list):
    my_dict = {}
    if list is not None:
        for i in list:
            my_dict[i] = my_dict.get(i, 0) + 1
    
    dup_list = []
    for i, count in my_dict.items():
        if count > 1:
            dup_list.append(i)
      
    return dup_list
    
    # my_dict = {}
    # for num in nums:
    #     my_dict[num] = my_dict.get(num, 0) + 1
        
    # dup_list = []
    # for num, count in my_dict.items():
    #     if count > 1:
    #         dup_list.append(num)
        
    # return dup_list



# Test cases
if __name__ == "__main__":
    print ( find_duplicates([1, 2, 3, 4, 5]) )
    print ( find_duplicates([1, 1, 2, 2, 3]) )
    print ( find_duplicates([1, 1, 1, 1, 1]) )
    print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
    print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
    print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
    print ( find_duplicates([]) )



    """
        EXPECTED OUTPUT:
        ----------------
        []
        [1, 2]
        [1]
        [3, 4]
        [1, 2, 3]
        [1, 2, 3]
        []

    """

