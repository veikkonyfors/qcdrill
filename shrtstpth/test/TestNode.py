'''
Created on Dec 3, 2021

@author: pappa
'''
import unittest
from costmatrix import CostMatrix
from costrow import CostRow

class TestNode(unittest.TestCase):
    
    def setUp(self):
        self.cost_matrix=CostMatrix()
        self.cost_matrix.add_line(CostRow(0,"9, 8, 7"))
        self.cost_matrix.add_line(CostRow(1,"6,5,4"))
        self.cost_matrix.add_line(CostRow(2,"3,2,1"))
        self.node=self.cost_matrix.get_node(1,1)

    def test_node_str(self):
        node=self.cost_matrix.get_node(1, 2)
        result = node.__str__()
        self.assertEqual(result, '1, 2, 4', "test_node_str failed")

    def test_get_cost(self):
        result = self.node.get_cost()
        self.assertEqual(result, 5, "test_get_cost failed")

