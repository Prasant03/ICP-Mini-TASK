import hashlib
import time
import random

class MiningSimulation:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.target = "0" * difficulty

    def mine_block(self, data):
        nonce = 0
        start_time = time.time()
        attempts = 0

        while True:
            attempts += 1
            block_string = f"{data}{nonce}"
            hash_result = hashlib.sha256(block_string.encode()).hexdigest()

            if hash_result.startswith(self.target):
                end_time = time.time()
                return {
                    "hash": hash_result,
                    "nonce": nonce,
                    "attempts": attempts,
                    "time_taken": end_time - start_time
                }

            nonce += 1

def main():
    # Test different difficulty levels
    difficulties = [2, 3, 4, 5]
    
    for difficulty in difficulties:
        print(f"\n=== Mining with difficulty {difficulty} ===")
        miner = MiningSimulation(difficulty)
        
        # Generate random data
        data = f"Block data {random.randint(1000, 9999)}"
        
        print(f"Starting mining for data: {data}")
        result = miner.mine_block(data)
        
        print(f"Block mined: {result['hash']}")
        print(f"Nonce: {result['nonce']}")
        print(f"Attempts: {result['attempts']}")
        print(f"Time taken: {result['time_taken']:.4f} seconds")

if __name__ == "__main__":
    main() 