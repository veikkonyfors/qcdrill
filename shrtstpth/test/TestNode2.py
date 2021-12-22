'''
Created on Dec 11, 2021

@author: pappa
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_node_str(self):
        result = self.node1.get_adjacent_nodes()
        self.assertEqual(result, '1, 2, 6', "get_adjacent_nodes failed")
        
    def get_cost(self):
        result = self.node1.get_adjacent_nodes()
        self.assertEqual(result, '1, 2, 6', "get_adjacent_nodes failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()