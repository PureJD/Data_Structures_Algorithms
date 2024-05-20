class Node:
    '''This is the node constructor which will be called every time a new node is made'''
    def __init__(self, value):
        self.value = value
        self.next = None 

class Queue:
    '''This function will be called when initally creating the queue'''
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node
        self.length = 1
        
    def print_queue(self):
        '''This function will print the queue'''
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def enqueue(self, value):
        '''This function will add a new node to the end of the queue'''
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
            
         
            
    
my_queue = Queue(5)
my_queue.print_queue()
print('Add a new node to the queue')
my_queue.enqueue(6)
my_queue.print_queue()

        