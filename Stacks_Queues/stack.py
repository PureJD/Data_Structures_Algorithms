class Node:
    '''This is the node constructor which will generate new nodes when needed with the value requested'''
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    '''This will creat the inital stack, to be used to init a new stack'''
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        '''This function will loop through a stack and print out all values that have been saved in the nodes'''
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def push(self, value):
        '''This will create a new node and place it at the head of the stack'''
        new_node = Node(value)
        if self.height < 1:
            self.top = new_node
        else:
            new_node.next = self.top 
            self.top = new_node
        self.height += 1

    def pop(self):
        '''This will move the head of the stack down and then remove the node that is currently a head by removing next pointer'''
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp   

test_stack = Stack(4)
test_stack.print_stack()
print('Time to add a new node to the stack')
test_stack.push(5)
test_stack.print_stack()
print('Now a node will be removed from the top')
test_stack.pop()
test_stack.print_stack()