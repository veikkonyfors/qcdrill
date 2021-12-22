'''
Created on Dec 11, 2021

@author: pappa
'''

from node import Node

class Route():
    '''
    Route, list of nodes on the route
    '''

    def __init__(self):
        '''
        Instantiated with initial node
        '''
        self.nodes=[]
        #self.nodes.append(node)
        
    def add_node(self, node):
        self.nodes.append(node)

    def get_route(self):
        return self.nodes

    def get_cost(self):
        cost=0
        for node in self.nodes: cost=cost+node.get_cost()
        return cost

    def exists_already(self,node):
        for nodei in self.nodes:
            if nodei == node: return True
        return False
    
    def add_node_if_not_exists_already(self,node):
        if not self.exists_already(node): self.add_node(node)

    def __str__(self):
        return '\n'.join(str(p) for p in self.nodes) 
