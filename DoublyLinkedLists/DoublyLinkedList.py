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
    
    def pop(self):
        '''This function will remove the final node and then move the tail across and severe the links'''
        if self.length == 0:
            return None
        if self.length == 1:
            self.head == None
            self.tail == None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp 
    
    def prepend(self, value):
        '''This function will take a value, create a node, link the pointers to the new node and then move the head'''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        '''This function will remove the first node and then remove the pointers which attach to it'''
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp 

    def get(self, index):
        '''This function has been optimised for doubly linked lists. It will move through elements from the head if the index is in the first half, and from the tail if in the second half'''
        if index < 0 or index >= self.length:
            return None
        if index > self.length / 2:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        return temp
    
    def set_value(self, index, value):
        '''This function will take one of two paths to the index depending on the position in the list. It will then change the value at the requested index to the specified value'''
        if index < 0 or index >= self.length:
            return None
        if index > self.length / 2:
            temp = self.tail
            for _ in range(self.length - index -1):
                temp = self.tail.prev
            temp.value = value
            return temp
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
            return temp
        
    def insert(self, index, value):
        '''This function will locate the index, place a variable either side of where the new node is to go, then adjust the pointers using to variables to attach the node in the appropriate position'''
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next 
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        '''This function will remove a node at a certain index by adjusting pointers'''
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        before = self.get(index -1)
        after = before.next
        before.next = after.next
        after.next.prev = before
        after.next = None
        after.prev = None
        self.length -= 1
        return True

    def find_middle_node(self):
        '''This method will loop through the entire list, the fast travelling at twice the speed as slow. Once fast has reached the end, slow would have been mid way and it will be returned. This method will return the value to the right when there are an even amount of nodes'''
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow #In order to see value for testing change this to 'print(slow.value)'
    
    def reverse(self):
        '''This method will swap the head and tail. It will then use variables to move through the list and the temp variable changes the pointer for each node'''
        if self.length < 2: 
            return False
        current = self.head
        prev = None
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return True
            
    def find_middle_node(self):
        '''This method will loop through the entire list, the fast travelling at twice the speed as slow. Once fast has reached the end, slow would have been mid way and it will be returned.'''
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow  
    
    def has_loop(self):
        '''This method is similar to the find the middle method, however it also checks to see if the values of fast and slow are the same at any stage as this would mean there is a loop in the nodes through caseless linking.'''
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def shuffle(self):
        '''This function will shuffle the nodes in a list by means of reversing the list, finding the middle two digits, splitting the list into two and then reattaching the first half to the end. If a more complete shuffle is required, run the splitting and reattaching in a loop. Do not run the whole function again as it will undo the shuffle.  '''
        if self.length < 2:
            return None
        if self.length == 2 or self.length == 3:
            return self.reverse()
        self.reverse()
        temp_right = self.find_middle_node()
        temp_left = temp_right.prev
        temp_right.prev = None
        temp_left.next = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.head = temp_right
        self.tail = temp_left
        return True
        
        
        
        
            


        


        
        

test_list = Doublylinkedlist(5)
test_list.print_list()
print('Now a test for appending the value 6')
test_list.append(6)
test_list.append(7)
test_list.append(7)
test_list.append(4)
test_list.append(8)
test_list.append(9)
test_list.print_list()       
print('Now the pop function will remove a number from the end')
test_list.pop()
test_list.print_list() 
print('Time to prepend a value')
test_list.prepend(8)
test_list.print_list()
print('time to pop the first element')
test_list.pop_first()
test_list.print_list()
print('Time for a get function that will return a requested node. This will only return the node, to see the node value add .value after the return')
test_list.get(2)
test_list.print_list()
print('time to test changing a value at a certain index')
test_list.set_value(2, 10)
test_list.print_list() 
print('time to insert a new node at a certain index')
test_list.insert(4, 11)
test_list.print_list()
print('The remove functoin will remove a node in the list')
test_list.remove(3)
test_list.print_list()
print('Testing the find middle function ')
test_list.find_middle_node() 
test_list.print_list()
print('Time to reverse the list')
test_list.reverse()
test_list.print_list()
print('The next function will find the middle node and return it. In order to see the node result please change return to print and then add .value to test')
test_list.find_middle_node()
test_list.print_list()
print('Time to shuffle the nodes')
test_list.shuffle()
test_list.print_list()
