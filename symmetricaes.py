#One symmetric message authentication code


import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

msg = b'secret message to unitedfront'
#key = Fernet.generate_key()
#cipher_suite = Fernet(key)
aad = b"Help is on the way"
key = AESGCM.generate_key(bit_length=128)
esgcm = AESGCM(key)
nonce = os.urandom(12)

encrypt_msg = esgcm.encrypt(nonce, msg, aad)

decrrypt_msg = esgcm.decrypt(nonce, encrypt_msg, aad)

print(f"Cipher: {encrypt_msg}")
print(f"Decrypted Text: {decrrypt_msg}")