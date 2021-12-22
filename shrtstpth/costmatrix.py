class CostMatrix():
    
    """
    Costs, class to deal with costs matrix as rows of Nodes.
    Each rows' nodes are initialized per the line in costsfile.
    
    E.g.
    [[Node(0,0,9),Node(0,1,8),Node(0,2,7],
    [Node(1,0,6),Node(1,1,5),Node(1,2,4],
    [Node(2,0,3),Node(2,1,2),Node(2,2,1]]
    
    """
    
    def __init__(self):
        self.cost_matrix=[]
        
    def add_line(self, costrow):
        """
        add_line, add one line of costs
        """
        self.cost_matrix.append(costrow)
    
    def get_num_lines(self):
        return len(self.cost_matrix)
    
    def get_num_columns(self):
        return self.cost_matrix[0].get_num_columns()
    
    def get_node(self,row,column):
        return self.cost_matrix[row].get_node(column)

    def get_adjacent_nodes(self,node):
        adjacent_nodes=[]
        #r-1c-1, r-1c,r-1c+1, rc-1, rc+1, r+1c-1, r+1c, r+1c+1
        for row in range(node.row-1,node.row+2): # row+2 not included in range
            for col in range(node.col-1,node.col+2):
                if row<0 or col<0: continue # row or column was 0
                if row>=self.get_num_lines() or col>=self.get_num_columns(): continue # row or column was the last one
                if row==node.row and col==node.col: continue # node itself
                adjacent_nodes.append(self.get_node(row,col))
        return adjacent_nodes
    
    def is_adjacent(self,node1, node2):
        if node1.row==node2.row and node1.col==node2.col: return False
        if abs(node1.row-node2.row)>1 or abs(node1.col-node2.col): return False
        return True
    
    def __str__(self):
        return '\n'.join(str(p) for p in self.cost_matrix) 
    