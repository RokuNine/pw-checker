# this file decrypts the text file containing the passwords
from cryptography.fernet import Fernet

# getting the encrypted key
with open('key.key', 'rb') as filekey:
	key = filekey.read()

fernet = Fernet(key)

# opening the encrypted file
with open('./pwtext.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and writing the decrypted data
with open('./pwtext.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
