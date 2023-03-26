import bitcoin as b
import hashlib

# Authenticate with blockchain.com/api to get transaction information
API_KEY = 'your API key here'
api = b.BlockchainAPI(API_KEY)

# Get balance and transaction count for the specified Bitcoin address
bitcoin_address = 'your bitcoin address here'
balance, transaction_count = api.get_balance(bitcoin_address)

# Use the Bitcoin library to get the address's public keys
address = b.BitcoinAddress.from_address(bitcoin_address)
public_keys = address.public_keys()

# Print the desired information about the address in the desired format:
print('1. Bitcoin Address: ' + bitcoin_address + '\n')
print('2. Address Balance: ' + str(balance) + "\n")
print('3. Address Transaction Count: ' + str(transaction_count) + "\n")

# Print addresses in different formats
print('4. P2SH Address: ' + b.P2SH.to_p2sh(public_keys[0]))
print('5. P2PKH Address: ' + b.P2PKH.to_p2kh(public_keys[0]))

# Print the address's private keys (not recommended to display private keys in public):
print('6. Private Keys: ' + (public_keys[0].a, public_keys[0].b, public_keys[0].private).encode('utf-8'))
