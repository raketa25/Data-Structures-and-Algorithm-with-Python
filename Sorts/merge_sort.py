"""
This code defines a function `merge` that takes two sorted lists as input and merges them into a single sorted list. The function uses two pointers to traverse both lists and compare their elements, appending the smaller element to the combined list. Once one of the lists is fully traversed, any remaining elements from the other list are appended to the combined list. Finally, the merged list is returned.
The test case at the end demonstrates the function by merging two sorted lists and printing the result, which should be a single sorted list containing all the elements from both input lists.
"""

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i <len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
            
    while i < len(list1):
        combined.append(list1[i])
        i += 1
        
    while j < len(list2):
        combined.append(list2[j])
        j += 1
        
    return combined

# Test case
if __name__ == "__main__":
    print(merge([1,2,7,8], [3,4,5,6]))



    """
        EXPECTED OUTPUT:
        ----------------
        [1, 2, 3, 4, 5, 6, 7, 8]
        
    """