'''
Created on Nov 19, 2021

@author: pappa
'''
import unittest

from blockchain.blockchain import BlockChain

class TestBlockChain(unittest.TestCase):
    def testTestBlockChain(self):
        block_chain = BlockChain()
        result = block_chain.get_chain()
        print('result: ' + result)
        self.assertEqual(result,
        {"length": 1, "chain": [{"index": 0, "transactions": [], "timestamp": 1637335736.7861102, "previous_hash": "0", "nonce": 0, "hash": "cd73d2f2b6eda026ff27a0362eaee0489a2b7fda1265db5631768e50838a0748"}]},"Oops")
        #{"length": 1, "chain": [{"index": 0, "transactions": [], "timestamp": 1637335565.7916698, "previous_hash": "0", "nonce": 0, "hash": "ab5cb9516b0cdcffd9e1344fb2d83cb7c67e37804b89bc71cb33471ee3163ba0"}]}

