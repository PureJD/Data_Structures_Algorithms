class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 



#Test code 
test_linked_list = LinkedList(23)
print(test_linked_list.tail.value)
print(test_linked_list.tail.value)
print(test_linked_list.length)



##test


