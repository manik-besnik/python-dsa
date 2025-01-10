class Graph:
    
    def __init__(self):
        self.adjacency_list = {}
        
    def add_node(self, node):
        self.adjacency_list[node] = []
        
    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
        
    def remove_edge(self,node1, node2):
        self.adjacency_list[node1].remove(node2)
        self.adjacency_list[node2].remove(node1)
        
    def remove_node(self, removeNode):
        
        if removeNode in self.adjacency_list:
            
            for node, neighbour in self.adjacency_list.items():
                if removeNode in self.adjacency_list[node]:
                    self.adjacency_list[node].remove(removeNode)
                    
            self.adjacency_list.pop(removeNode)
            
    def display(self):
        for node, neighbour in self.adjacency_list.items():
            print(f"Node is {node} and Neighbour is {neighbour}")
            
            
graph = Graph()


graph.add_node("A")
graph.add_node("B")
graph.add_edge("A","B")


graph.display()
print('first time')

graph.add_node("C")
graph.add_edge("A","C")
graph.add_edge("B","C")

graph.display()
print('second time')
graph.remove_edge("C",'A')
graph.display()