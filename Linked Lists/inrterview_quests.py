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

    def getlength(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def partition_list(self, x):
        dummy1 = Node(0)
        dummy2 = Node(0)

        prev1 = dummy1
        prev2 = dummy2

        temp = self.head
        while temp:
            if temp.value < x:
                prev1.next = temp
                prev1 = temp
            else:
                prev2.next = temp
                prev2 = temp
            temp = temp.next

        prev1.next = dummy2.next
        prev2.next = None

        self.head = dummy1.next


    def remove_duplicates(self):
        temp = self.head
        prev = None
        seen_values = set()

        while temp:
            if temp.value in seen_values:
                prev.next = temp.next
            else:
                seen_values.add(temp.value)
                prev = temp
            temp = temp.next


    def binary_to_decima(self):
        decimal_value = 0
        temp = self.head

        while temp:
            decimal_value = decimal_value * 2 + temp.value
            temp = temp.next
        return decimal_value
    

    def reverse_between(self, start_index, end_index):
        if start_index == end_index:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(start_index):
            prev = prev.next

        current = prev.next
        for _ in range(end_index - start_index):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        self.head = dummy.next
    
    def find_kth_from_end(ll, k):
        slow = ll.head
        fast = ll.head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow.value

# ===================== Example usage ===================== #
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print("Original list:")
my_linked_list.print_list()
print('\n')
print("Middle node value:", my_linked_list.find_middle_node())

my_linked_list.reverse()
print("\nReversed list:")
my_linked_list.print_list()
print('\n')

print("Length of the list:", my_linked_list.getlength())