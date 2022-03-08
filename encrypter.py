# This file encrypts the text file containing the passwords
# using the cryptography module and generates a secure key
from cryptography.fernet import Fernet

# key generator
key = Fernet.generate_key()

# writes the key
with open('key.key', 'wb') as key_file:
  key_file.write(key)

# reads the key
with open('key.key', 'rb') as filekey:
  key = filekey.read()

f = Fernet(key)

# opens the original text file
with open('./pwtext.txt', 'rb') as file:
  original = file.read()

# encrypts the file
encrypted = f.encrypt(original)

# writes the encrypted file
with open('./pwtext.txt', 'wb') as encrypted_file:
  encrypted_file.write(encrypted)
