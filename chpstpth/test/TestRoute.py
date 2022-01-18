'''
Created on Dec 11, 2021

@author: pappa
'''
import unittest
from route import Route
from costmatrix import CostMatrix
from costrow import CostRow


class TestRoute(unittest.TestCase):

    def setUp(self):
        self.cost_matrix=CostMatrix()
        self.cost_matrix.add_line(CostRow(0,"19, 18, 17"))
        self.cost_matrix.add_line(CostRow(1,"16,15,14"))
        self.cost_matrix.add_line(CostRow(2,"6,5,4"))
        self.node1 = self.cost_matrix.get_node(0,1)
        self.node2 = self.cost_matrix.get_node(1,2)
        self.node3 = self.cost_matrix.get_node(2,1)
        self.route=Route()
        self.route.add_node(self.node1)
        self.route.add_node(self.node2)
        self.route.add_node(self.node3)


    def test_route_str(self):
        result = self.route.__str__()
        self.assertEqual(result, '0, 1,  18\n1, 2, 14\n2, 1, 5', "test_route_str failed")
        
    def test_get_cost(self):
        result = self.route.get_cost()
        self.assertEqual(result, 37, "test_route_str failed")
        
    def test_exists_already_true(self):
        result = self.route.exists_already(self.node2)
        self.assertEqual(result, True, "test_exists_already_true failed")
        
    def test_exists_already_false(self):
        result = self.route.exists_already(self.cost_matrix.get_node(2,2))
        self.assertEqual(result, False, "test_exists_already_false failed")
        
    def test_add_if_not_exists_already_noadd(self):
        self.route.add_node_if_not_exists_already(self.node1)
        result = self.route.__str__()
        print(result)
        self.assertEqual(result, '0, 1,  18\n1, 2, 14\n2, 1, 5', 
                         "test_add_if_not_exists_already_noadd failed")
        
    def test_add_if_not_exists_already_add(self):
        self.route.add_node_if_not_exists_already(self.cost_matrix.get_node(2,2))
        result = self.route.__str__()
        print(result)
        self.assertEqual(result, '0, 1,  18\n1, 2, 14\n2, 1, 5\n2, 2, 4', 
                         "test_add_if_not_exists_already_add failed")

    def test_remove(self):
        self.route.remove_node()
        result = self.route.__str__()
        print(result)
        self.assertEqual(result, '0, 1,  18\n1, 2, 14', 
                         "test_add_if_not_exists_already_noadd failed")
        
    def test_remove_empty(self):
        self.route.remove_node()
        self.route.remove_node()
        self.route.remove_node()
        result = self.route.__str__()
        print(result)
        self.assertEqual(result, '', 
                         "test_add_if_not_exists_already_noadd failed")

    def tearDown(self):
        pass
