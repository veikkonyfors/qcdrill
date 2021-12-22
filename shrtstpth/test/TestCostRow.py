'''
Created on Dec 9, 2021

@author: pappa
'''

import unittest
from costrow import CostRow
from node import Node

class TestCostRow(unittest.TestCase):
    
    def setUp(self):
        self.cost_row=CostRow(0,'1,2,3')
        
    def test_costrow_str(self):
        result = self.cost_row.__str__()
        self.assertEqual(result, '0, 0, 1, 0, 1, 2, 0, 2, 3', "test_costrow_str failed")
        
    def test_get_node(self):
        result = self.cost_row.get_node(1).__str__()
        self.assertEqual(result, '0, 1, 2', "test_get_node failed")
