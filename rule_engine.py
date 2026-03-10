import pandas as pd
from datetime import datetime
import os

# Get the absolute path to transactions.json
script_dir = os.path.dirname(os.path.abspath(__file__))  # folder of this script
file_path = os.path.join(script_dir, "..", "Ingestion", "transactions.json")
file_path = os.path.abspath(file_path)  # ensures Windows-friendly absolute path
transactions = []
with open(file_path, "r") as f:
    for line in f:
        transactions.append(pd.read_json(line, typ='series'))

df = pd.DataFrame(transactions)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Step 2: Flag suspicious transactions
df['flag'] = 'Clean'

# Rule 1: High Value Transactions (> R10,000)
df.loc[df['amount'] > 10000, 'flag'] = 'High Value'

# Rule 2: Impossible Travel
df = df.sort_values(['user_id', 'timestamp'])
df['prev_location'] = df.groupby('user_id')['location'].shift(1)
df['prev_time'] = df.groupby('user_id')['timestamp'].shift(1)
df['time_diff'] = (df['timestamp'] - df['prev_time']).dt.total_seconds() / 60

df.loc[(df['location'] != df['prev_location']) & (df['time_diff'] <= 10), 'flag'] = 'Impossible Travel'

# Step 3: Save processed transactions to CSV
output_path = os.path.join(os.path.dirname(__file__), "processed_transactions.csv")
df.to_csv(output_path, index=False)
print(f"Processed transactions saved to {output_path}")

# Optional: print flagged transactions
print(df[['user_id', 'amount', 'location', 'timestamp', 'flag']])