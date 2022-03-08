from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('key.key', 'wb') as key_file:
  key_file.write(key)
with open('key.key', 'rb') as filekey:
  key = filekey.read()
f = Fernet(key)
with open('./pwtext.txt', 'rb') as file:
  original = file.read()
encrypted = f.encrypt(original)
with open('./pwtext.txt', 'wb') as encrypted_file:
  encrypted_file.write(encrypted)