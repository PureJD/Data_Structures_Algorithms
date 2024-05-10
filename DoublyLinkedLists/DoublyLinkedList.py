class Node():
    '''This creates nodes as it is called in various functions. It creates a previous value as well as a next'''
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class Doublylinkedlist():
    '''This creates the inital list'''
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        '''This function will cycle through the list and print all the nodes values'''
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        '''This function will create a new node and point the next and previous values before moving the tail across to the end'''
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True 
        

test_list = Doublylinkedlist(5)
test_list.print_list()
print('Now a test for appending the value 6')
test_list.append(6)
test_list.print_list()        
