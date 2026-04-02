"""
This code defines a Node class and a LinkedList class. The Node class represents an individual node in the linked list, containing a value and a reference to the next node. The LinkedList class manages the linked list, allowing for the creation of a new linked list with an initial value, printing the list, and appending new values to the end of the list.
The LinkedList constructor initializes the linked list with a single node containing the provided value. It sets both the head and tail of the list to this new node and initializes the length of the list to 1. The print_list method traverses the linked list and prints the value of each node. The append method creates a new node with the given value and adds it to the end of the list, updating the tail reference and incrementing the length of the list.
"""
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            removed_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed_node
        
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index == 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True



# Example usage:
my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.prepend(11)

my_linked_list.print_list()
print('\n')

my_linked_list.prepend(13)
my_linked_list.print_list()
