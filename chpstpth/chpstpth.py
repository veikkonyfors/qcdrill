'''
# chpstpth, CHeaPeSTPaTH, traverse nxm cost_matrixm to find the most cost effective route.
# Each node consists of a cost amount, which is added to the cost of route, if route goes through this node.
# Traversion can start and end from whichever node. Tested only from a node on first line and ending on the last.
# A hop from node to node may be taken into any direction, i.e. right, downright, down, downleft, left, upleft, up and upright.
# Recursive implementation.
# Just in order to familiarize on a NP-Hard problem, later trying to solve it in Quantum way
'''

import sys

from costrow import CostRow
from costmatrix import CostMatrix
from traveler import Traveler
from route import Route

print("Find cheapest path on a costmatrix\n")

if __name__ == '__main__':
    
    cost_matrix=CostMatrix()
    all_routes=[]
    
    # Read input matrix into cost_matrix object
    with open(sys.argv[1], 'r') as infile:
        for index, line in enumerate(infile):
            cost_matrix.add_line(CostRow(index, line))
    
    print(str(cost_matrix.get_num_lines())+"x"+str(cost_matrix.get_num_columns())+"\n")
    print(cost_matrix)
    
    traveler=Traveler(cost_matrix, Route(), all_routes)
    start_node=cost_matrix.get_node(0, 1)
    destination_node=cost_matrix.get_node(2, 1)
    
    traveler.travel_recursively(start_node, destination_node)
    i=0; cost=0; all_routes=traveler.get_all_routes()
    for route in all_routes:
        print('\nRoute '+str(i));
        print(route.__str__())
        route_cost=route.get_cost()
        if cost==0 or route_cost < cost : cost=route_cost; cheapest_route=i;
        i+=1
        
    print("\nCheapest route: "+str(cheapest_route)+", cost="+str(cost))
    print(all_routes[cheapest_route])



