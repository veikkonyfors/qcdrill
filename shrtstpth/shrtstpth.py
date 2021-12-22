#
# shrtstpth, SHoRTeSTPaTH, traverse n lines by 3 columns cost_matrixmatrix to find the most cost effective route.
#
# In order to familiarize on techniques to eventually solve Traveling Salesman Problem in Quantum way

import sys

from costrow import CostRow
from costmatrix import CostMatrix
from traveler import Traveler

print("Find shortest path on a costmatrix\n")

cost_matrix=CostMatrix()

# Read input matrix into cost_matrix object
with open(sys.argv[1], 'r') as infile:
    for index, line in enumerate(infile):
        cost_matrix.add_line(CostRow(index, line))

print(str(cost_matrix.get_num_lines())+"x"+str(cost_matrix.get_num_columns())+"\n")
print(cost_matrix)

traveler=Traveler(cost_matrix)
start_node=cost_matrix.get_node(0, 1)
destination_node=cost_matrix.get_node(2, 1)

traveler.travel(start_node, destination_node)
print(traveler.get_route())

# One should find the least expensive route from costmatrix[0][1] to costmatrix[len(2)][len(costmatrix[1])
# Traversefrom startto end

#costmatrix.traverse(0,1,1,1) # Not yet implemented

