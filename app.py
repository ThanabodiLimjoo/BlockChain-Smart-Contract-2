import web3
from web3 import Web3
import json
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

url = 'http://127.0.0.1:8545'
web3 = Web3(Web3.HTTPProvider(url))
abi = """[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_fname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_lname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_gpax",
				"type": "string"
			}
		],
		"name": "edit",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_fname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_lname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_gpax",
				"type": "string"
			}
		],
		"name": "post",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "_flag",
				"type": "bool"
			}
		],
		"name": "setFlag",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAll",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "fname",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "lname",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "gpax",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "flag",
						"type": "bool"
					}
				],
				"internalType": "struct Smartcontract.Student[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getByID",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "numElements",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "stu",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "fname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "lname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "gpax",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "flag",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
"""

class Contract:
    def __init__(self, abi_address):
        self.contract = web3.eth.contract(address=abi_address, abi=abi)
        web3.eth.defaultAccount = web3.eth.accounts[0]

    def post(self, id, fname, lname, gpax):
        tx_hash = self.contract.functions.post(id, fname, lname, gpax).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)

    def getAll(self):
        return self.contract.functions.getAll().call()

    def getByID(self, id):
        return self.contract.functions.getByID(id).call()

    def edit(self, id, fname, lname, gpax):
        tx_hash = self.contract.functions.edit(id,fname, lname, gpax).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)

    def setFlag(self, id, flag):
        tx_hash = self.contract.functions.setFlag(id, flag).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)

app = Flask(__name__)
CORS(app)

@app.route('/post', methods=['POST'])
def post():
    req = request.get_json()
    abi_address = req['abi_address']
    id = req['id']
    fname = req['fname']
    lname = req['lname']
    gpax = req['gpax']
    value = Contract(abi_address).post(id, fname, lname, gpax)
    return jsonify("success")

@app.route('/getAll', methods=['POST'])
def getAll():
    req = request.get_json()
    abi_address = req['abi_address']
    value = Contract(abi_address).getAll()
    return jsonify(value)

@app.route('/getByID', methods=['POST'])
def getByID():
    req = request.get_json()
    abi_address = req['abi_address']
    id = req['id']
    value = Contract(abi_address).getByID(id)
    return jsonify(value)

@app.route('/edit', methods=['POST'])
def edit():
    req = request.get_json()
    abi_address = req['abi_address']
    id = req['id']
    fname = req['fname']
    lname = req['lname']
    gpax = req['gpax']
    value = Contract(abi_address).edit(id, fname, lname, gpax)
    return jsonify("success")

@app.route('/setFlag', methods=['POST'])
def setFlag():
    req = request.get_json()
    abi_address = req['abi_address']
    id = req['id']
    flag = req['flag']
    value = Contract(abi_address).setFlag(id, flag)
    return jsonify("success")

app.run(debug=True)