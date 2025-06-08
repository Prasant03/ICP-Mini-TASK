# 🧱 Mini Task 1: Build & Explain a Simple Blockchain

This project is a hands-on exercise to understand how a blockchain works by simulating its basic components and mechanisms using Python. It is divided into three code-based parts:

* ✅ Blockchain Structure Simulation
* ✅ Proof-of-Work (Mining)
* ✅ Consensus Mechanisms: PoW, PoS, and DPoS

## 📁 Files Included

| Filename | Description |
|----------|-------------|
| blockchain_simulation.py | Simulates 3 connected blocks in a blockchain and demonstrates chain tampering |
| mining_simulation.py | Simulates Proof-of-Work mining by finding a hash that satisfies difficulty |
| consensus_demo.py | Demonstrates PoW, PoS, and DPoS consensus logic with mock validators |

## 🧪 How to Run

Make sure Python 3 is installed. Then run:

```bash
python blockchain_simulation.py
python mining_simulation.py
python consensus_demo.py
```

## 🔹 Features

1. **Blockchain Structure**
   - Creates a chain of 3 blocks
   - Demonstrates immutability through hash linking
   - Shows how tampering breaks the chain

2. **Mining Simulation**
   - Implements Proof-of-Work
   - Adjustable difficulty levels
   - Performance metrics (time and attempts)

3. **Consensus Mechanisms**
   - Proof of Work (PoW)
   - Proof of Stake (PoS)
   - Delegated Proof of Stake (DPoS)

## 📝 Requirements

- Python 3.x
- hashlib (built-in)
- time (built-in)
- random (built-in) 