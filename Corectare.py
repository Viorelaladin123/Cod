import requests
import json
import random

# Your Etherscan API key
api_key = "JGJKCQ58HUCXTHA4A4GKJ4UBU3RI7TM26F"

# Function to generate random Ethereum private key
def generate_ethereum_private_key():
 # Generate random private key
 y
 private_key = hex(random.getrandbits(256))[2:]
 return private_key

# Function to get Ethereum account balance from Etherscan
def get_ethereum_balance(address):
 # Define Etherscan API URL
 base_url = base_url = "https://api.etherscan.io/api"
 endpoint = "/?module=account&action=balance&address="
 url = f"{base_url}{endpoint}{address}&tag=latest&apikey={api_key}"

 # Send HTTP GET request to Etherscan Etherscan API
 response = requests.get(url)

 # Parse response JSON
 if response.status_code == 200:
 balance = json.loads(response.text)['result']
 return balance
 return balance
 else:
 return "API Error"

# Generate 10 Ethereum private keys and check their balance
for i in range(10):
 # Generate random Ethereum private key
 private_key = generate_ethereum_private_key()

 # Derive the Ethereum public erive the Ethereum public key from the private key
 public_key = "0x" + hex(int(private_key, 16) ** 2 + 7)[2:].zfill(128)

 # Derive the Ethereum address from the public key
 address address = "0x" + hex(int(public_key[2:], 16) % (2 ** 160))[2:].zfill(40)

 # Get the Ethereum account balance for the address from Etherscan
 balance = get_ethereum_balance(address)

 # Print the Ethereum private key, public key, address, and balance
 print(f"Private Key: {private_key}")
 print(f"Public Key: {public_key}")
 print(f"Address: {address}")
 ress: {address}")
 print(f"Balance: {balance}\n")
