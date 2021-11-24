class CostLine:
    """
    Costline, class for one line of costsfile
    """

    def __init__(self, line):
        """
        Init, with costline
        """
        self.rowColumns=[]
        self.rowColumns=line.strip().split(",")
    
    def getNumColumns(self):
        return len(self.rowColumns)
    
    def getColumns(self):
        return self.rowColumns
    
    def __str__(self):
        return ', '.join(str(p) for p in self.rowColumns)
 
    
    