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
    
    def pop(self):
        '''This method allows for the final node to be removed and for the tail to be redirected to the correct node'''
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next         
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        '''A method that will create a new node with value, place this at the front and have the head point at it'''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        '''Pops the first element in the list. Moves the head pointer to the right and then removes the first element'''
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
        '''A method that will provide the node at a certain index'''
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value): 
        '''A method that will take arugements for index and value and change the index to the value using a temporay pointer variable'''
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return temp 
    
    def insert(self, index, value):
        'A method that will take an index and a value, create a new node and point the node either side of the index to it'
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.head
        for _ in range(index -1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        '''Remove method will move the previous pointer before the index to the node after the index node. It wil then move the index node to point at nothing, removing the node'''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp 

        

    

            




        
            



#Test code 

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
print('Pre pop')
my_linked_list.print_list()
my_linked_list.pop()
print('After the pop')
my_linked_list.print_list()
print('Linked list after prepend')
my_linked_list.prepend(1)
my_linked_list.print_list()
print('after second pop')
my_linked_list.pop_first()
my_linked_list.print_list()
print('requesting index 3...')
print(my_linked_list.get(2))
print('testing changing value 2 to 5')
my_linked_list.set_value(0, 5)
my_linked_list.print_list()
print('time to insert a value ')
my_linked_list.insert(1, 6)
my_linked_list.print_list()
print('testing the remove of index 1')
my_linked_list.remove(1)
my_linked_list.print_list() 



