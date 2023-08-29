import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Alphabet is the combination of letters, digits and special characters
alphabet = letters + digits + special_chars

# define password length
password_len = 12

password = ''

for i in range(password_len):
    password += ''.join(secrets.choice(alphabet))

print(f"Password is: {password}")

