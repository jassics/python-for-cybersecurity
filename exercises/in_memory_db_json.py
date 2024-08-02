# The problem requires implementing an in-memory key-value store
# where you can set a key-value pair and
# retrieve the value of a key.

# Example:
# db.set(101, ["Sanjeev", "ProdSec"])
# db.set(102, ["Deep", "DevSecOps"])
# db.get(102)
# Think of command line for n inputs, set for n inputs, then based on command implement get, delete
# Example:
# Choose below options for operations:
#     1. set/create entries
#     How many entries: 2
#     emp_id: input
#     emp_details: input([])
#     2. get emp_id details
#     3. delete emp_id details
#     4. update emp_id details
# use loop for interactive session
# usr argparse for cmd options
# use json to store the data for permanent use
# handle as much error as you can, also some edge cases
import argparse
import json
import os

class DB:
    def __init__(self, filename='db.json'):
        self.filename = filename
        self.dic = self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.dic, f, indent=4)

    def set(self, key: int, value: list) -> None:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        if not isinstance(value, list):
            raise TypeError("Value must be a list")
        if key in self.dic:
            raise ValueError(f"Key {key} already exists")
        self.dic[key] = value
        self.save()

    def get(self, key: int) -> list:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        if key in self.dic:
            return self.dic[key]
        else:
            print(f"No record found for emp id: {key}")
            return None

    def delete(self, key: int) -> None:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        if key in self.dic:
            print(f"Deleting emp id {key} details: {self.dic[key]}")
            del self.dic[key]
            print(f"Emp id {key} deleted successfully.")
            self.save()
        else:
            print(f"No record found for emp id: {key}")
        print(f"Current employee list: {self.dic}")

def main():
    db = DB()

    parser = argparse.ArgumentParser(description="Database operations")
    subparsers = parser.add_subparsers(dest="command")

    # Set command
    set_parser = subparsers.add_parser("set", help="Set a new entry")
    set_parser.add_argument("key", type=int, help="Key (employee ID)")
    set_parser.add_argument("value", nargs='+', help="Value (employee details)")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get an entry")
    get_parser.add_argument("key", type=int, help="Key (employee ID)")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an entry")
    delete_parser.add_argument("key", type=int, help="Key (employee ID)")

    args = parser.parse_args()

    if args.command == "set":
        try:
            db.set(args.key, args.value)
            print(f"Set key {args.key} with value {args.value}")
        except (TypeError, ValueError) as e:
            print(e)

    elif args.command == "get":
        try:
            details = db.get(args.key)
            if details:
                print(f"Emp id {args.key} details: {details}")
        except TypeError as e:
            print(e)

    elif args.command == "delete":
        try:
            db.delete(args.key)
        except TypeError as e:
            print(e)

    else:
        while True:
            print("\nChoose an operation:")
            print("1. Set a new entry")
            print("2. Get an entry")
            print("3. Delete an entry")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                try:
                    key = int(input("Enter key (employee ID): "))
                    value = input("Enter value (employee details separated by spaces): ").split()
                    db.set(key, value)
                    print(f"Set key {key} with value {value}")
                except (TypeError, ValueError) as e:
                    print(e)

            elif choice == '2':
                try:
                    key = int(input("Enter key (employee ID): "))
                    details = db.get(key)
                    if details:
                        print(f"Emp id {key} details: {details}")
                except TypeError as e:
                    print(e)

            elif choice == '3':
                try:
                    key = int(input("Enter key (employee ID): "))
                    db.delete(key)
                except TypeError as e:
                    print(e)

            elif choice == '4':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
