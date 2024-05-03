class Node():
    '''A class which creates the individual node'''
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    '''A class which will create the inital linked list'''
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        '''Method that will append a new node to the end of the current list'''
        appended_node = Node(value)
        if self.head is None:
            self.head = appended_node
            self.tail = appended_node
        else:
            self.tail.next = appended_node
            self.tail = appended_node
        self.length += 1
        return True 



#Test code 
my_linked_list = LinkedList(2)
my_linked_list.append(56)
my_linked_list.append(24234232)
add_value = 2
for i in range(34):
    my_linked_list.append(add_value)
    add_value += 1

my_linked_list.print_list()



