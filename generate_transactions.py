import random
import json
from datetime import datetime
import time
import os

# Ensure the file is saved in the same folder as the script
file_path = os.path.join(os.path.dirname(__file__), "transactions.json")

users = ['U1001', 'U1002', 'U1003', 'U1004']
locations = ['Durban', 'Johannesburg', 'Cape Town', 'Pretoria']

def generate_transaction():
    return {
        "user_id": random.choice(users),
        "amount": round(random.uniform(10, 20000), 2),
        "location": random.choice(locations),
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    for _ in range(20):  # generate 20 transactions
        tx = generate_transaction()
        print(json.dumps(tx))
        # Append to JSON file
        with open(file_path, "a") as f:
            f.write(json.dumps(tx) + "\n")
        time.sleep(1)