import random
import csv
from datetime import datetime, timedelta

def generate_trade_data():
    num_users = 25
    trade_data = []

    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)

    current_date = start_date
    while current_date <= end_date:
        for user_id in range(1, num_users + 1):
            trade_value = random.randint(0, 100)
            trade_date = current_date.strftime("%m-%d-%Y")
            trade_data.append((user_id, trade_value, trade_date))
        current_date += timedelta(days=1)

    return trade_data

# Generate trade data
data = generate_trade_data()

# Define the CSV file path
csv_file_path = "trade_data.csv"

# Write the data to the CSV file
with open(csv_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["user_id", "trade_value", "trade_date"])  # Write header row
    writer.writerows(data)  # Write trade data rows

print(f"Trade data exported to: {csv_file_path}")
