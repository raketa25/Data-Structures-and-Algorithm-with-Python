"""
This code defines a Node class and a DoublyLinkedList class. The Node class has an initializer that takes a value and sets the data, next, and prev attributes. The DoublyLinkedList class has an initializer that takes a value, creates a new node with that value, and sets the head, tail, and length attributes of the list. The print_list method is defined to traverse the list and print the value of each node.


"""
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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