"""
This module implements a stack data structure using a list. The Stack class provides methods for common stack operations such as push, pop, peek, and checking if the stack is empty. Additionally, it includes a method to reverse a string using the stack and a function to check for balanced parentheses in a given string.
"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0
    
    def size(self):
        return len(self.stack_list)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack_list[-1]

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack_list.pop()
    
    def reverse_string(self, string):
        stack = Stack()
        for char in string:
            stack.push(char)
        
        reversed_string = ""
        while not stack.is_empty():
            reversed_string += stack.pop()
        
        return reversed_string
    

def is_balanced_parentheses(string):
    myStack = Stack()
    parentheses_map = {')': '(', 
                       '}': '{', 
                       ']': '['}

    for char in string:
        if char in parentheses_map.values():
            myStack.push(char)

        elif char in parentheses_map.keys():
            if myStack.is_empty() or myStack.pop() != parentheses_map[char]:
                return False

    return myStack.is_empty()


if __name__ == "__main__":
    from stack_list import StackList

    stack = StackList()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())  # Output: 3
    print(stack.peek())  # Output: 2
    print(stack.is_empty())  # Output: False
    print(stack.size())  # Output: 2
    print('\n')

    # Test reverse_string method
    original_string = "Hello, World!"
    reversed_string = stack.reverse_string(original_string)
    print(reversed_string)  # Output: !dlroW ,olleH
    print('\n')

    # Test is_balanced_parentheses function
    def test_is_balanced_parentheses():
        try:
            assert is_balanced_parentheses('((()))') == True
            print('Test case 1 passed')
        except AssertionError:
            print('Test case 1 failed')

        try:
            assert is_balanced_parentheses('()') == True
            print('Test case 2 passed')
        except AssertionError:
            print('Test case 2 failed')

        try:
            assert is_balanced_parentheses('(()())') == True
            print('Test case 3 passed')
        except AssertionError:
            print('Test case 3 failed')

        try:
            assert is_balanced_parentheses('(()') == False
            print('Test case 4 passed')
        except AssertionError:
            print('Test case 4 failed')

        try:
            assert is_balanced_parentheses('())') == False
            print('Test case 5 passed')
        except AssertionError:
            print('Test case 5 failed')

        try:
            assert is_balanced_parentheses(')(') == False
            print('Test case 6 passed')
        except AssertionError:
            print('Test case 6 failed')

        try:
            assert is_balanced_parentheses('') == True
            print('Test case 7 passed')
        except AssertionError:
            print('Test case 7 failed')

        try:
            assert is_balanced_parentheses('()()()()') == True
            print('Test case 8 passed')
        except AssertionError:
            print('Test case 8 failed')

        try:
            assert is_balanced_parentheses('(())(())') == True
            print('Test case 9 passed')
        except AssertionError:
            print('Test case 9 failed')

        try:
            assert is_balanced_parentheses('(()()())') == True
            print('Test case 10 passed')
        except AssertionError:
            print('Test case 10 failed')

        try:
            assert is_balanced_parentheses('((())') == False
            print('Test case 11 passed')
        except AssertionError:
            print('Test case 11 failed')

    test_is_balanced_parentheses()
