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

    def reverse(self):
        '''This method will swap the head and tail. It will then use three variables to move through the list and the temp variable changes the pointer for each node'''
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

    def find_kth_from_end(self, k):
        '''This method will set fast to the value of K in steps ahead into the list. Both fast and slow then move through the list one step at a time. Once fast reaches the end, we can be sure that slow is at the requested place'''
        slow = fast = self.head   
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def remove_duplicates(self):
        '''This method will remove duplicates from the list. It utilises the set() function in order to keep a record of all seen values '''
        if not self.head or not self.head.next:
            return  # If the list is empty or has only one element, return
        seen = set()  # This will store the values we've seen so far
        current = self.head
        seen.add(current.value)  # Add the first node's value to the set
        while current.next:  # Iterate until the end of the list
            if current.next.value in seen:
                current.next = current.next.next  # Skip the duplicate
                self.length -= 1  # Decrease the length if you maintain it
            else:
                seen.add(current.next.value)  # Add new value to the set
                current = current.next  # Move to the next node
                
    def shuffle(self):
        '''This function will shuffle the nodes in a list by means of reversing the list, finding the middle two digits, splitting the list into two and then reattaching the first half to the end. If a more complete shuffle is required, run the splitting and reattaching in a loop. Do not run the whole function again as it will undo the shuffle.  '''
        if self.length < 2:
            return None
        if self.length == 2 or self.length == 3:
            return self.reverse()
        self.reverse()
        temp_left = self.find_middle_node()
        temp_right = temp_left.next
        temp_left.next = None
        self.tail.next = self.head
        return True
        
        

    

            




        
            



#Test code 

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
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
print('Lets try and reverse the remaining')
my_linked_list.reverse()
my_linked_list.print_list()
print('Seeking that middle node now (no representation in terminal return changed to print)')
my_linked_list.find_middle_node()
print('Now checking if the linked list has an accidential loop (Returns true or false)')
my_linked_list.has_loop()
print('The next method will look for the element which is a specified distance from the end of the the list. K. I will request 2 from the end of our list. This method is working, change return to print to see the node and add .value to see the value')
my_linked_list.find_kth_from_end(2)
print('The remove duplicates function will now eliminate a 5 due to it being duplicate')
my_linked_list.remove_duplicates()
my_linked_list.print_list()
print(my_linked_list.length)
print('Test of the shuffle function')

my_linked_list.shuffle()
my_linked_list.print_list()



