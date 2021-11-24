#
# shrtstpth, SHoRTeSTPaTH, traverse n lines by 3 columns costsmatrix to find the most cost effective route.
#
# In order to familiarize on techniques to eventually solve Traveling Salesman Problem in Quantum way

import sys

from costline import CostLine
from costs import Costs 

print("Find shortest path on a costmatrix\n")

costs=Costs()

# Read input matrix into Costs object
with open(sys.argv[1], 'r') as infile:
    for line in infile:
        costLine=CostLine(line)
        costs.addLine(costLine)

print(str(costs.getNumLines())+"x"+str(costs.getNumColumns())+"\n")
print(costs)

# One should find the least expensive route from costs[0][1] to costs[len(2)][len(costs[1])
# Traversefrom startto end

#costs.traverse(0,1,1,1) # Not yet implemented