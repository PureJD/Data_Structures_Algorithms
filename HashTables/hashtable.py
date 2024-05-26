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
            
hash_table = HashTable()
print('The below will print the hash table with all values currently set to None')
hash_table.print_table() 
