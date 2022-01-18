'''
Created on Dec 9, 2021

@author: pappa
'''
import unittest
from costmatrix import CostMatrix
from costrow import CostRow

class TestCostMatrix(unittest.TestCase):
    
    def setUp(self):
        self.cost_matrix=CostMatrix()
        self.cost_matrix.add_line(CostRow(0,"9, 8, 7"))
        self.cost_matrix.add_line(CostRow(1,"6,5,4"))

    def test_add_line(self):
        result = self.cost_matrix.__str__()
        #print(result)
        self.assertEqual(result, '0, 0, 9, 0, 1,  8, 0, 2,  7\n1, 0, 6, 1, 1, 5, 1, 2, 4'
                         , "test_add_line failed")

    def test_get_num_lines(self):
        result = self.cost_matrix.get_num_lines()
        #print(result)
        self.assertEqual(result, 2
                         , "test_add_line failed")
        
    def test_get_num_columns(self):
        result = self.cost_matrix.get_num_columns()
        #print(result)
        self.assertEqual(result, 3, "test_add_line failed")
        
    def test_get_node(self):
        result = self.cost_matrix.get_node(1,2).__str__()
        #print(result)
        self.assertEqual(result, '1, 2, 4', "test_add_line failed")
        
    def test_get_adjacent_nodes_01(self):
        result = '\n'.join(str(p) for p in self.cost_matrix.get_adjacent_nodes(self.cost_matrix.get_node(0,1)))
        self.assertEqual(result, '0, 0, 9\n0, 2,  7\n1, 0, 6\n1, 1, 5\n1, 2, 4', "tst_get_adjacent_nodes_01 failed")

    def test_get_adjacent_nodes_11(self):
        result = '\n'.join(str(p) for p in self.cost_matrix.get_adjacent_nodes(self.cost_matrix.get_node(1,1)))
        self.assertEqual(result, '0, 0, 9\n0, 1,  8\n0, 2,  7\n1, 0, 6\n1, 2, 4', "test_get_adjacent_nodes_11 failed")