import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

msg = b'secret message to unitedfront'
aad = b"Help is on the way"
key = AESGCM.generate_key(bit_length=128)
esgcm = AESGCM(key)
nonce = os.urandom(12)

def main():
    encrypt_msg = esgcm.encrypt(nonce, msg, aad)
    decrypt_msg = esgcm.decrypt(nonce, encrypt_msg, aad)
    print(f"Cipher: {encrypt_msg}")
    print(f"Decrypted Text: {decrypt_msg}")

if __name__ == '__main__':
    main()

