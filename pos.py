import hashlib

class Block:
    def __init__(self, data, previous_hash, stake_amount):
        self.data = data
        self.previous_hash = previous_hash
        self.stake_amount = stake_amount
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # calculate the hash of the block data
        return hashlib.sha256(self.data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # create the first block in the chain
        return Block("Genesis Block", "0", 0)

    def add_block(self, data, stake_amount):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash, stake_amount)
        self.chain.append(new_block)

# create a new blockchain
blockchain = Blockchain()

# add some blocks to the chain
blockchain.add_block("Block 1", 100)  # 100 units of stake
blockchain.add_block("Block 2", 50)   # 50 units of stake
blockchain.add_block("Block 3", 75)   # 75 units of stake
blockchain.add_block("Block 4", 10000)   # 10000 units of stake

# print out the contents of the chain
for block in blockchain.chain:
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Stake Amount: {block.stake_amount}")
    print(f"Hash: {block.hash}")

#Rich brooo


