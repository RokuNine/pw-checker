import requests
import hashlib
import sys
import cryptography.exceptions
from cryptography.fernet import Fernet

# This function captures the api from a password checker website for use in later functions.
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

# This function checks if passwords have been leaked and creates a counter for each time the password has been leaked.
def get_password_leaks_count(hashes, hash_to_check):
  #This tuple splits the SHA-1 hash and the counter apart for each password for a proper counter.
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

# This function converts the password strings into a SHA-1 hash from the hashlib package that the api is able to read.
def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

'''
# This function uses inputs from the terminal to check for password safety.
def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times. Consider changing it.')
    else:
      print(f'{password} not found.')
  return 'Finished'
'''

# opens the key file to recognize the encryption
with open('key.key', 'rb') as filekey:
  key = filekey.read()

fernet = Fernet(key)

with open('./pwtext.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
  
# This except statement catches exceptions from the cryptography module in case the file is ran again without the encrypter
# This passes the decryption command error if the text file is not encrypted.
try:
  decrypted = fernet.decrypt(encrypted)
# writes the file in decrypted mode
  with open('./pwtext.txt', 'wb') as dec_file:
      dec_file.write(decrypted)
except cryptography.exceptions.InvalidKey:
  pass
except cryptography.fernet.InvalidToken:
  pass


# This function reads from the text file of passwords
def main():
    with open('./pwtext.txt', mode='r') as pw_file:
        lines = pw_file.readlines()
        lines = [line.rstrip() for line in lines]
    for password in lines:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. Consider changing it.')
        else:
            print(f'{password} not found.')
    return 'Finished.'

if __name__ == '__main__':
  sys.exit(main())
