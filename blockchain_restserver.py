'''
Created on Nov 10, 2021

@author: pappa
'''

#
# Needs to be on parent directory for blockchain. Otherwise gives blockchain is not a module
#
import json
from flask import Flask #, request

from blockchain.blockchain import BlockChain

#import requests
 
app =  Flask(__name__)

blockchain = BlockChain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
app.run(debug=True, port=5000)