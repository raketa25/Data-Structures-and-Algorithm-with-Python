"""
This  code demonstrate how pointers work under the hood.
""" 
num1 = 11

num2 = num1

print("Before num2 is value is updated: ")
print("num1 = ", num1)
print("num2 = ", num2)
print('\n')

# Numbers id inside our computer system.
print("num1 points to:", id(num1))
print("num2 points to:", id(num2))
print('\n')

num2 = 22

print("After value is updated: ")
print("num1 = ", num1)
print("num2 = ", num2)
print('\n')

# Numbers id inside our computer system after updates.
print("num1 points to:", id(num1))
print("num2 points to:", id(num2))
print('\n')

# Use of dictionaries
dict1 = {
    'value': 11
}

dict2 = dict1

print("Before num2 is value is updated: ")
print("dict1 = ", dict1)
print("dict2 = ", dict2)
print('\n')

# Numbers id inside our computer system.
print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print('\n')

dict2['value'] = 22

print("After value is updated: ")
print("dict1 = ", dict1)
print("dict2 = ", dict2)
print('\n')

# Numbers id inside our computer system after updates.
print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
