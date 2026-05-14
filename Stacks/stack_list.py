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