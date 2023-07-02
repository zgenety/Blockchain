import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
import config

# Set up web3 connection
provider_url = os.environ.get("CELO_PROVIDER_URL")
w3 = Web3(Web3.HTTPProvider(provider_url))
assert w3.is_connected()

# Add PoA middleware to web3.py instance
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

abi = config.abi
contract_address = config.contract_address

contract = w3.eth.contract(address=contract_address, abi=abi)