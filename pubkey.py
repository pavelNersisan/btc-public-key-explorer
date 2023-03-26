from bitcoinrpc.authproxy import AuthServiceProxy
from bitcoinrpc.connection import Connection
from hashlib import sha256
from bson import PyBSONDocument
from pprint import pprint

def bitcoin_address_lookup(bitcoin_address):
    # Initialize the bitcoin RPC connection with blockchain.com/api
    rpc_password = b'your rpc password'
    rpc_user = b'serializer'
    rpc_connection = Connection(host='b.eu.blockchain.info', port=4443, user=rpc_user, password=rpc_password, disabled_ssl=True)

    # Retrieve the public key, balance and number of transactions from blockchain.com/api
    json_message = rpc_connection.getinfo(bitcoin_address)
    json_message = json_message['txs']
    public_key = sha256(json_message['verack'].encode('utf-8')).hexdigest().decode('utf-8')
    balance = json_message['unconfirmed'] / 100000000
    transaction_count = len(json_message['txs']) + 1
    p2sh_public_key = json_message[json_message.keys()[1]].encode('utf-8')
    p2sh_address = json_message[json_message.keys()[1]].decode('utf-8')

    print(f'1. {bitcoin_address}\n2. {balance:,}\n3. {transaction_count}\n4. {p2sh_address}:{p2sh_public_key}\n')

    with AuthServiceProxy(auth=rpc_password, user=rpc_user, host='127.0.0.1', port=8332) as proxy:
        proxy.getblockchaininfo()
        print(f'5. {bitcoin_address}\n6. {proxy.getbalance(bitcoin
