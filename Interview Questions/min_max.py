"""
This function takes a list of numbers as input and returns a tuple containing the maximum and minimum values in the list. It iterates through the list once, comparing each number to the current maximum and minimum values, and updates them accordingly. If the input list is empty, it returns (None, None).
"""

def find_max_min(myList):
    if not myList:
        return None, None 
    
    max_val = myList[0]
    min_val = myList[0]

    for num in myList:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
        result = (max_val, min_val)
    return result

# Example usage:
numbers = [3, 1, 4, 1, 5, 9]
max_value, min_value = find_max_min(numbers)
print(f"Maximum: {max_value}, Minimum: {min_value}")


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
"""