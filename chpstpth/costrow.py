from node import Node

class CostRow:
    """
    CostRow, class for one line of costsfile
    Holds costs as Node objects
    
    E.g. [Node(2,0,3),Node(2,1,2),Node(2,2,1]] for 2.line of 3, 2, 1 in the costs file
    """

    def __init__(self, rownum, line):
        """
        Init, with costline
        """
        self.row_nodes=[]
        for column, cost in enumerate(line.strip().split(",")):
            self.row_nodes.append(Node(rownum,column,cost))
    

    def get_num_columns(self):
        return len(self.row_nodes)
      
    def get_columns(self):
        return self.row_nodes
            
    def get_node(self,column):
        return self.row_nodes[column]
    
    def __str__(self):
        return ', '.join(str(p) for p in self.get_columns())
 
    
    