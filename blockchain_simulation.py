import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

def main():
    # Create blockchain
    blockchain = Blockchain(difficulty=4)
    
    print("Mining block 1...")
    block1 = Block(1, "Block 1 Data", "")
    blockchain.add_block(block1)
    
    print("Mining block 2...")
    block2 = Block(2, "Block 2 Data", "")
    blockchain.add_block(block2)
    
    print("Mining block 3...")
    block3 = Block(3, "Block 3 Data", "")
    blockchain.add_block(block3)
    
    # Print blockchain
    print("\nBlockchain:")
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Nonce: {block.nonce}")
    
    # Demonstrate tampering
    print("\n--- Tampering with Block 1 ---")
    blockchain.chain[1].data = "Hacked Data"
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()
    
    print("\nBlockchain after tampering:")
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
    
    print("\nIs blockchain valid?", blockchain.is_chain_valid())

if __name__ == "__main__":
    main() 