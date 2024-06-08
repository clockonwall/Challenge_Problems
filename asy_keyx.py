# importing libraries
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes


# generating private key
private_key = rsa.generate_private_key(
   public_exponent=65537,
   key_size=2048,
)


# generating public key and serialising
public_key = private_key.public_key()
pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)
pem.splitlines()[0]


# signing the message which allows anyone with the public key to confirm attribution
message = b"nice job encrypting that thing dude"
signature = private_key.sign(
   message,
   padding.PSS(
           mgf=padding.MGF1(hashes.SHA256()),
           salt_length=padding.PSS.MAX_LENGTH
   ),
   hashes.SHA256()
  
)


# verification section
public_key = private_key.public_key()
public_key.verify(
   signature,
   message,
   padding.PSS(
       mgf=padding.MGF1(hashes.SHA256()),
       salt_length=padding.PSS.MAX_LENGTH
   ),
   hashes.SHA256()
)


# encryption process
ciphertext = public_key.encrypt(
   message,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)


# decryption process
plaintext = private_key.decrypt(
   ciphertext,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)
if plaintext == message :
   print(plaintext)
else:
    print("error")
