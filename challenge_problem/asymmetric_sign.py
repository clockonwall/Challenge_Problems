from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import os

def create_a_personal_keypair():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return public_key, private_key

def sign(private_key, message):
    signature = private_key.sign(message)
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message)
        print("Signature successfully verified! You can trust this message.")
    except Exception as e:
        print(f"Signature verification failed. Do not trust this message. Error: {e}")





def main():
    public_key, private_key = create_a_personal_keypair()
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("Public Key (PEM):")
    print(public_key_pem.decode('utf-8'))
    plaintext = "The bad guys will never be able to read this"
    plaintext_bytes = plaintext.encode('utf-8')
    signature = sign(private_key, plaintext_bytes)
    print(f"Signature: {signature.hex()}")
    verify_signature(public_key, plaintext_bytes, signature)



if __name__ == '__main__':
    main()