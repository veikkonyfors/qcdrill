'''
Created on Dec 3, 2021

@author: pappa
'''

from route import Route
from node import Node

class Traveler():
    
    def __init__(self,cost_matrix,route,all_routes): 
        self.cost_matrix=cost_matrix
        self.route=route
        self.all_routes=all_routes
        
    def travel_recursively(self,start_node,destination_node):
        ''' traverse, to pick up the least expensive route from start to end
        :param start_node: Node to start with
        :type start_node: Node
        :param destination_node: Node to end with
        :type destination_node: Node
        '''
        
        assert type(start_node) is Node, 'Need Node { start_node }'
        assert type(destination_node) is Node, 'Need Node { destination_node }'


        if start_node==destination_node:
            self.route.add_node(destination_node)
            #print(self.route.__str__())
            self.all_routes.append(self.route.copy_route())
            #print("Route:\n"+str(self.route))
            #print("all: "+self.all_routes[len(self.all_routes)-1].__str__())
            return
        
        self.route.add_node(start_node)
        
        #traveler=Traveler(self.cost_matrix,self.route,self.all_routes)
        for node in self.cost_matrix.get_adjacent_nodes(start_node):
            if not self.route.exists_already(node):
                Traveler(self.cost_matrix,self.route,self.all_routes).travel_recursively(node, destination_node)
                self.route.remove_node()
    
    def get_route(self):
        return self.route
    
    def get_all_routes(self):
        return self.all_routes
    
    def propagate_nodes(self, node):
        pass
    
    def __str__(self):
        return self.cost_matrix.__str__()+\
            self.route.__str__() +\
            '\n'.join(str(p) for p in self.all_routes) 