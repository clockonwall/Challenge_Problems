from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# sender generates key pair
sender_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048  # 2048-bit key is a good balance of security and performance
)
sender_public_key = sender_private_key.public_key()

# reciever generates key pair
rec_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048  # 2048-bit key is a good balance of security and performance
)
rec_public_key = rec_private_key.public_key()

# signing the message which allows anyone with the public key to confirm attribution
message = b"nice job encrypting that thing dude"
signature = sender_private_key.sign(
    message,
    padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# sender generates a symmetric key to encrypt the key before sending
symmetric_key = AESGCM.generate_key(bit_length=256)  # Generate a random 256-bit symmetric key, 

# Message is encrypted with AES-GCM
aesgcm = AESGCM(symmetric_key)
nonce = os.urandom(12)
aad = b"this is used to authenticate"
ciphertext = aesgcm.encrypt(nonce, message, aad)

# sender encrypts the symmetric key with the reciever's public key
# can only be decrypted with reciever's private key
encrypted_symmetric_key = rec_public_key.encrypt(
    symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask Generation Function which adds an element of randomness therefore more security; 
        algorithm=hashes.SHA256(),  # Hashing algorithm
        label=None  
    )
)

# reciever decrypts the symmetric key with their private key
decrypted_symmetric_key = rec_private_key.decrypt(
    encrypted_symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  
        algorithm=hashes.SHA256(),  
        label=None  
    )
)

# verification section
sender_public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)    

# decryption process using AES-GCM again
plaintext = aesgcm.decrypt(nonce, ciphertext, aad)

if plaintext == message :
    print("Decryption successful", plaintext)
else:
     print("Decryption error")

if symmetric_key == decrypted_symmetric_key:
    print("Key:", decrypted_symmetric_key) # both users can now use this key for secure communication
else:
    print("Key exchange failed.")

