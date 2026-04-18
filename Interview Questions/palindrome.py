def is_palindrome(s):
    # Remove spaces and convert to lowercase
    # cleaned_s = s.replace(" ", "").lower()
    cleaned_s = str(cleaned_s)  # Convert to string if it's not already
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]


# Example usage
input_string = [1, 2, 3, 2, 1]
print(is_palindrome(input_string))  # Output: True
print("\n")
input_string = "hello"
print(is_palindrome(input_string))  # Output: False
