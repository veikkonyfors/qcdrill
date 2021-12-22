'''
Created on Dec 3, 2021

@author: pappa
'''

from route import Route
from node import Node

class Traveler():
    
    def __init__(self,cost_matrix,route):
        self.cost_matrix=cost_matrix
        self.start_node=None
        self.destination_node=None
        self.initial_node=True
        self.route=route
        
    def travel_recursively(self,start_node,destination_node):
        ''' traverse, to pick up the least expensive route from start to end
        :param start_node: Node to start with
        :type start_node: Node
        :param destination_node: Node to end with
        :type destination_node: Node
        '''
        
        assert type(start_node) is Node, 'Need Node { start_node }'
        assert type(destination_node) is Node, 'Need Node { destination_node }'
            
        self.start_node=start_node
        self.destination_node=destination_node
        
        #self.route.add_node_if_not_exists_already(start_node)
        traveler=Traveler(self.cost_matrix,self.route)
        
        if start_node==destination_node:
            print("Route: "+str(self.route))
        else:
            for node in self.cost_matrix.get_adjacent_nodes(start_node): # First propagate adjacent nodes to route
                if not self.route.exists_already(node):
                    Traveler(self.cost_matrix,self.route).travel_recursively(node, destination_node)
                    
        return self.route
    
    def get_route(self):
        return self.route
    
    def propagate_nodes(self, node):
        pass
    
    def __str__(self):
        return str(self.start_node)+', '+str(self.destination_node)
    
    '''
    def tri_recursion(k):
      if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
      else:
        result = 0
      return result
        print("\n\nRecursion Example Results")
        tri_recursion(6)
    '''