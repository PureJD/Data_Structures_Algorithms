class HashTable:
    '''The constructor for the hash table'''
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        '''This function will create a hash'''
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        '''This function will print the table below'''
        for i, val in enumerate(self.data_map):
            print(i, ': ', val)
            
    def set_item(self, key, value):
        '''This function will set the value in the hash table'''
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        '''This function will get the value from the hash table'''
        index = self.__hash(key)  
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
            
hash_table = HashTable()
print('The below will print the hash table with all values currently set to None')
hash_table.print_table() 
print('The below will set the value of grapes to 10000')
hash_table.set_item('grapes', 10000)
hash_table.print_table()
print('The below code will test the get_item function')
print(hash_table.get_item('grapes'))
print(hash_table.get_item('apples'))    

