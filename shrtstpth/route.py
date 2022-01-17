'''
Created on Dec 11, 2021

@author: pappa
'''

from node import Node
from copy import copy

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
        
    def remove_node(self):
        self.nodes.pop()

    def get_route(self):
        return self.nodes
    
    def copy_route(self):
        copied_route=Route()
        for node in self.nodes:
           copied_route.add_node(node)
        return copied_route

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
        return '\n'.join(p.__str__() for p in self.nodes) 
