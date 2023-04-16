from web3 import Web3, AsyncWeb3

abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "temp_image",
				"type": "string"
			}
		],
		"name": "store",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "id",
				"type": "uint8"
			}
		],
		"name": "retrieve",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/b8a7bd302ec04e09bfa83b8e52434fcf'))