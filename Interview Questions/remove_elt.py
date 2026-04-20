"""
This function removes all occurrences of a specified value from a list of integers in-place and returns the new length of the list after removals. The order of elements can be changed, and it doesn't matter what you leave beyond the new length. The function iterates through the list, checking each element against the specified value. If it finds a match, it removes the element from the list. The function handles edge cases, such as an empty list, by returning 0. After processing the list, it returns the new length of the modified list.

"""

def remove_element(nums, val):
    # Checking for edge cases
    if not nums:
        return 0
    
    # Iterating through the list and removing the specified value

    i = 0     # Pointer for the position of the next element to keep.
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)  # Remove the element at index i.
        else:
            i += 1  # Move to the next index only if we didn't remove an element.
    # The length of the modified list is the new length after removals.
    new_length = len(nums)

    return new_length

# Example usage:
# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)
print("-----------------------------------")

# Test case 2: Removing a value that's located at the end of the list.
nums2 = [1, 2, 3, 4, 5, 6]
val2 = 6
print("\nRemove value", val2, "that's located at the end of the list.")
print("BEFORE:", nums2)
new_length2 = remove_element(nums2, val2)
print("AFTER:", nums2, "\nNew length:", new_length2)
print("-----------------------------------")

# Test case 3: Removing a value that's located at the start of the list.
nums3 = [-1, -2, -3, -4, -5]
val3 = -1
print("\nRemove value", val3, "that's located at the start of the list.")
print("BEFORE:", nums3)
new_length3 = remove_element(nums3, val3)
print("AFTER:", nums3, "\nNew length:", new_length3)
print("-----------------------------------")

# Test case 4: Attempting to remove a value from an empty list.
nums4 = []
val4 = 1
print("\nAttempt to remove value", val4, "from an empty list.")
print("BEFORE:", nums4)
new_length4 = remove_element(nums4, val4)
print("AFTER:", nums4, "\nNew length:", new_length4)
print("-----------------------------------")

# Test case 5: Removing all instances of a repeated value.
nums5 = [1, 1, 1, 1, 1]
val5 = 1
print("\nRemove all instances of value", val5, "from the list.")
print("BEFORE:", nums5)
new_length5 = remove_element(nums5, val5)
print("AFTER:", nums5, "\nNew length:", new_length5)
print("-----------------------------------")
