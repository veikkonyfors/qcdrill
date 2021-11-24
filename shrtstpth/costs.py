
class Costs():
    """
    Costs, class to deal with costs matrix
    """


    def __init__(self):
        self.costMatrix=[]
        
    def addLine(self, costLine):
        """
        addLine, add one line of costs
        """
        self.costMatrix.append(costLine)
    
    def getNumLines(self):
        return len(self.costMatrix)
    
    def getNumColumns(self):
        return self.costMatrix[0].getNumColumns()
    
    def __str__(self):
        return '\n'.join(str(p) for p in self.costMatrix) 
    