class Node():
    """
    Node, class to deal with single node of costmatrix matrix
    """
    
    def __init__(self,row, col,cost):
        self.row=row
        self.col=col
        self.cost=cost
        self.visited=False # Has this node already been visited in this route
    
    def get_cost(self):
        return int(self.cost)
    
    def __str__(self):
        return str(self.row)+', '+str(self.col)+', '+str(self.cost) 