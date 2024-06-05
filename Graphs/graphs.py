class Graph:
    '''This is the constructor for the graph which builds an empty dictionary'''
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        '''This method will print the nodes in the graph'''
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertext(self, vertex):
        '''This will allow you to create nodes in the graph'''
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
mygraph = Graph()
mygraph.add_vertext('Q')
mygraph.add_vertext('A')
mygraph.add_vertext('Q')
mygraph.print_graph()

    
    