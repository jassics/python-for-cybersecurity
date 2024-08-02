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

# Example usage
db = DB()

# Add employees
try:
    db.set(101, ["Jassi", "ProdSec"])
    db.set(102, ["Deep", "DevSecOps"])
    db.set(103, ["Deepraj Barman", "Developer"])
    db.set(104, ["Himanshu", "AppSec"])
    # Attempting to add an employee with an existing key
    db.set(101, ["Alex", "Security"])
except (TypeError, ValueError) as e:
    print(e)

# Get emp details
try:
    details = db.get(102)
    if details:
        print(f"Emp id 102 details: {details}")
except TypeError as e:
    print(e)

# Delete emp details
try:
    db.delete(102)
except TypeError as e:
    print(e)


