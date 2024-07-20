from cryptography.fernet import Fernet

key = Fernet.generate_key() 
cipher_suite = Fernet(key) 
message = "This is a secret message for a secret group. Not for crackers, but may be for Cryptanalyst!.".encode()

cipher_text = cipher_suite.encrypt(message) 
print('Cipher Text is: ' + str(cipher_text))

plain_text = cipher_suite.decrypt(cipher_text)
print('Here is the plain text:' + str(plain_text))

print('\nChecking if decrypted text is same as our message or not')

if plain_text == message: print("Yes both are same\n") 
