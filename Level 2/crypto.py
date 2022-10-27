
#  https://crackstation.net/
# Cryptography

#   - algorithm
#   - key
#   - hash
#   - encrypt/decrypt

#   - collision
#   - brute-force

import hashlib

secret_key = 'ybhkjbjk;lhkvbj'
password = '123456' + secret_key

hasher = hashlib.sha3_384(password.encode())
#password_hash = hasher.digest()
password_hash = hasher.hexdigest()

print(password_hash)
print(len(password_hash))
