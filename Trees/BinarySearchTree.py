class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    '''This constructor creates an empty binary search tree. The alternative would be to create the tree with the first node, this alternative version will be below'''
    def __init__(self):
        self.root = None
    '''  
    class BinarySearchTree():
        def __init__(self, value):
            new_node = Node(value)
            self.root = new_node
            self.length = 1
    '''   
    def insert(self, value):
        '''This method will create a pointer in temp and move through the list comparing the new node value to nodes to determine where it should be placed. If the value is less than current nodes it will move left and else it will move right. If the node value already exists in the tree, it will return false'''
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while (True):
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left 
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right
    
    def contains(self, value):
        '''This will search through the tree and return True if the sought value if found'''
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.left
            else:
                return True 
             
       
            
print('Initally make the list')   
my_b_search = BinarySearchTree()
my_b_search.insert(2)
print(my_b_search.root.value)
print('insert multiple values')
my_b_search.insert(1)
my_b_search.insert(3)
print(my_b_search.root.left.value)
print(my_b_search.root.right.value)
print(my_b_search.contains(2))
            
        
