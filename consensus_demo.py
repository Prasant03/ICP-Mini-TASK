import random
import time
from typing import List, Dict

class Validator:
    def __init__(self, name: str, power: int = 0, stake: int = 0):
        self.name = name
        self.power = power
        self.stake = stake
        self.votes = 0

class ConsensusDemo:
    def __init__(self):
        self.validators: List[Validator] = []
        self.delegates: List[Validator] = []

    def setup_validators(self):
        # Setup PoW validators (based on computational power)
        self.validators = [
            Validator("A", power=random.randint(50, 100)),
            Validator("B", power=random.randint(50, 100)),
            Validator("C", power=random.randint(50, 100))
        ]

        # Setup PoS validators (based on stake)
        for validator in self.validators:
            validator.stake = random.randint(100, 1000)

        # Setup DPoS delegates
        self.delegates = [
            Validator("Node1"),
            Validator("Node2"),
            Validator("Node3")
        ]

    def proof_of_work(self) -> Validator:
        # Simulate PoW by selecting validator with highest computational power
        return max(self.validators, key=lambda x: x.power)

    def proof_of_stake(self) -> Validator:
        # Simulate PoS by selecting validator with highest stake
        return max(self.validators, key=lambda x: x.stake)

    def delegated_proof_of_stake(self) -> Validator:
        # Simulate DPoS by having validators vote for delegates
        for validator in self.validators:
            # Each validator votes for a random delegate
            delegate = random.choice(self.delegates)
            delegate.votes += 1

        # Select delegate with most votes
        return max(self.delegates, key=lambda x: x.votes)

def main():
    demo = ConsensusDemo()
    demo.setup_validators()

    # Demonstrate PoW
    print("\n=== Proof of Work (PoW) ===")
    pow_winner = demo.proof_of_work()
    print(f"Winner: {pow_winner.name} (Power: {pow_winner.power})")
    print("Selected based on highest computational power")

    # Demonstrate PoS
    print("\n=== Proof of Stake (PoS) ===")
    pos_winner = demo.proof_of_stake()
    print(f"Winner: {pos_winner.name} (Stake: {pos_winner.stake})")
    print("Selected based on highest amount staked")

    # Demonstrate DPoS
    print("\n=== Delegated Proof of Stake (DPoS) ===")
    dpos_winner = demo.delegated_proof_of_stake()
    print(f"Winner: {dpos_winner.name} (Votes: {dpos_winner.votes})")
    print("Selected based on most community votes")

    # Print all validators and their attributes
    print("\n=== Validator Details ===")
    for validator in demo.validators:
        print(f"\nValidator {validator.name}:")
        print(f"Computational Power: {validator.power}")
        print(f"Stake: {validator.stake}")

if __name__ == "__main__":
    main() 