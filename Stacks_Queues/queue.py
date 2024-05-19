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
            
    
my_queue = Queue(5)
my_queue.print_queue()

        