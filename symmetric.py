#challenges One symmetric encryption algorithm

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)
message = b"Helloworld"


#encrpyt message

def encrypt_msg(data, key):
    Fernet(key)
    encrypt_msg = cipher_suite.encrypt(message)
    #print("Encrypt Message: {encrypt_msg}")
    return encrypt_msg

#decrypt message


def decrypt_msg(encrypt_msg, key):
    Fernet(key)
    decrypt_msg = cipher_suite.decrypt(encrypt_msg)
    #print("Encrypt Message: {encrypt_msg}")
    return decrypt_msg

def main():
    Fernet(key)
    encrypt_msg = cipher_suite(message)
    encrypt_msg = encrypt_msg(message, cipher_suite)    
    print(f"Cipher: {encrypt_msg}")
    decrypt_msg = decrypt_msg(encrypt_msg, cipher_suite)    
    print(f"Decrypted Text: {decrypt_msg}")
    


if __name__ == '__main__':
    main()
