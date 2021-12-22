'''
Created on Dec 3, 2021

@author: pappa
'''
import unittest
from traveler import Traveler
from costmatrix import CostMatrix
from costrow import CostRow
from route import Route


class TestTraveler(unittest.TestCase):

    def setUp(self):
        self.cost_matrix=CostMatrix()
        self.cost_matrix.add_line(CostRow(0,"9, 8, 7"))
        self.cost_matrix.add_line(CostRow(1,"6,5,4"))
        self.cost_matrix.add_line(CostRow(2,"6,5,4"))
        self.start_node = self.cost_matrix.get_node(0,1)
        self.end_node = self.cost_matrix.get_node(2,1)
        self.traveler = Traveler(self.cost_matrix,Route())

    def test_travel_recursively(self):
        routes=self.traveler.travel_recursively(self.start_node,self.end_node)
        #print(self.traveler)
        result = self.traveler.get_route()
        self.assertEqual(result, '0, 1,  8, 2, 1, 5', "tst_travel_recursively failed")

    def tst_traveler_traveled_str(self):
        self.traveler.travel_recursively(self.start_node,self.end_node)
        result = self.traveler.__str__()
        self.assertEqual(result, '0, 1,  8, 2, 1, 5', "tst_traveler_traveled_str failed")
        
    def tst_traveler_not_traveled_str(self):
        result = self.traveler.__str__()
        self.assertEqual(result, 'None, None', "tst_traveler_not_traveled_str failed")
        
    def tst_is_adjacent_false_same(self):
        result=self.traveler.is_adjacent(self.start_node, self.start_node)
        self.assertEqual(result, False, "tst_is_adjacent_false_same failed")
        
    def tst_is_adjacent_false_not_same(self):
        result=self.traveler.is_adjacent(self.start_node, self.end_node)
        self.assertEqual(result, False, "tst_is_adjacent_false_not_same failed")
        
    def tst_is_adjacent_true(self):
        result=self.traveler.is_adjacent(self.start_node, self.cost_matrix.get_node(1,1))
        self.assertEqual(result, True, "tst_is_adjacent_false_same failed")
        
    def tearDown(self):
        pass
