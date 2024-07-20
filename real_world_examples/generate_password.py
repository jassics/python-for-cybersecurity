import string
import secrets

def get_alphabet():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Alphabet is the combination of letters, digits and special characters
    alphabet = letters + digits + special_chars
    return alphabet

# Password constraints
# define password length, must be more than 8 chars
# at least 1 upper case, 1 lower case, 1 digit and 1 special character
password_len = int(input("Give password length(8 or more): "))
if password_len <8:
    exit("Length must be at least 8 characters")
password = ''

for i in range(password_len):
    password += ''.join(secrets.choice(get_alphabet()))

print(f"Password is: {password}")

