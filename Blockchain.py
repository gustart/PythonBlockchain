import hashlib
import datetime as dt

class Block:
  def __init__(self, transactions, previous_block_hash):
    self.transactions = transactions
    self.previous_block_hash = previous_block_hash
    self.timestamp = dt.datetime.now()
    self.hash = self.get_hash()

  def get_hash(self):
    header_bytes = (str(self.transactions) + 
                    str(self.previous_block_hash) + 
                    str(self.timestamp)).encode()
    return hashlib.sha256(header_bytes).hexdigest()

class Blockchain:
  def __init__(self):
    self.chain = [self.create_genesis_block()]

  def create_genesis_block(self):
    return Block([], "0")

  def add_block(self, transactions):
    previous_block_hash = self.chain[-1].hash
    new_block = Block(transactions, previous_block_hash)
    self.chain.append(new_block)

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current_block = self.chain[i]
      previous_block = self.chain[i-1]
      if current_block.hash != current_block.get_hash():
        return False
      if current_block.previous_block_hash != previous_block.hash:
        return False
    return True

# Test the blockchain
blockchain = Blockchain()
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")

print(blockchain.chain[0].hash)
print(blockchain.chain[1].hash)
print(blockchain.validate_chain())
