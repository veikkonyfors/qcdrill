"""
Gencosts, generate costmatrix file

Usage: gencosts.py outputfile lines columns[3]

"""
import sys
import random

outf=sys.argv[1]
lines=int(sys.argv[2])
columns=3 if len(sys.argv)<4 else int(sys.argv[3])
separator=", "
mincost, maxcost = 0, 33
print(lines, columns)

with open(sys.argv[1], 'w') as outfile:
    for line in range(lines):
        for col in range(columns):
            outfile.write(str(random.randint(mincost, maxcost))+separator)
        outfile.write("\n")
            
        


