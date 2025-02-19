import uuid
import csv

def read_users_from_csv(filename):
    """Read user data from CSV and return a list of dictionaries."""
    users = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["isAdmin"] = row["isAdmin"].lower() == "true"
                users.append(row)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Creating a new one.")
    return users

def write_users_to_csv(filename, users):
    """Write user data to CSV."""
    fieldnames = ["userId", "username", "password", "isAdmin"]
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(users)
    except IOError:
        print(f"Error: Unable to write to {filename}.")


