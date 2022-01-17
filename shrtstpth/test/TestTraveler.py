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
        self.all_routes=[]
        self.traveler = Traveler(self.cost_matrix,Route(),self.all_routes)


    def test_travel_recursively(self):
        routes=self.traveler.travel_recursively(self.start_node,self.end_node)
        #print(self.traveler)
        result = self.traveler.get_all_routes()
        i=0
        for route in result:
            print('\nRoute '+str(i));
            print(route.__str__()); i+=1
        print("\n\nresult[117]:\n"+result[117].__str__())
        self.assertEqual(result[117].__str__(), '0, 1,  8\n1, 2, 4\n2, 2, 4\n1, 1, 5\n2, 1, 5', "tst_travel_recursively failed")
        self.assertEqual(result[79].__str__(), '0, 1,  8\n1, 0, 6\n2, 0, 6\n2, 1, 5', "tst_travel_recursively failed")
        self.assertEqual(result[0].__str__(), '0, 1,  8\n0, 0, 9\n1, 0, 6\n1, 1, 5\n0, 2,  7\n1, 2, 4\n2, 1, 5', "tst_travel_recursively failed")

    def tst_traveler_traveled_str(self):
        self.traveler.travel_recursively(self.start_node,self.end_node)
        result = self.traveler.__str__()
        print(result)
        self.assertIn(result[0:20], '0, 1,  8, 2, 1, 5- 0, 0, 9, 0, 1,  8, 0, 2,  7', "tst_traveler_traveled_str failed")
        self.assertIn(result, '0, 1,  8, 2, 1, 5', "tst_traveler_traveled_str failed")
        
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
