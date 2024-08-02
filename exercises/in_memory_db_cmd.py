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

import argparse

class DB:

    def __init__(self):
        self.dic = {}

    def set(self, key: int, value: list) -> None:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        if not isinstance(value, list):
            raise TypeError("Value must be a list")
        if key in self.dic:
            raise ValueError(f"Key {key} already exists")
        self.dic[key] = value

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
        else:
            print(f"No record found for emp id: {key}")

        print(f"Current employee list: {self.dic}")

def main():
    parser = argparse.ArgumentParser(description="Database operations")
    subparsers = parser.add_subparsers(dest="command")

    # Set command
    set_parser = subparsers.add_parser('set', help="Set a new entry")
    set_parser.add_argument("key", type=int, help="Key (employee ID)")
    set_parser.add_argument("value", type=str, nargs='+', help="Value (employee details)")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get an entry")
    get_parser.add_argument("key", type=int, help="Key (employee ID)")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an entry")
    delete_parser.add_argument("key", type=int, help="Key (employee ID)")

    args = parser.parse_args()
    db = DB()

    # Example preloaded entries
    try:
        db.set(101, ["Jassi", "ProdSec"])
        db.set(102, ["Deep", "DevSecOps"])
        db.set(103, ["Deepraj Barman", "Developer"])
        db.set(104, ["Himanshu", "AppSec"])
    except (TypeError, ValueError) as e:
        print(e)

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

if __name__ == "__main__":
    main()

