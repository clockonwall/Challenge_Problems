from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
msg = b"Hello SUnny wolrd"



def main():
    encrpty_msg = cipher.encrypt(msg)
    decrypt_msg = cipher.decrypt(encrpty_msg)
    print(f"Cipher: {encrpty_msg}")
    print(f"Decrypted Text: {decrypt_msg}")

if __name__ == '__main__':
    main()


    

