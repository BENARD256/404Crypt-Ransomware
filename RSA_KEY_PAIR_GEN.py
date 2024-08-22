from Crypto.PublicKey import RSA

# This is used by Attacker to generate Key Pairs
key = RSA.generate(2048)


private_key = key.export_key()

public_key = key.public_key().export_key()


with open("private.pem", "wb") as pr_key:
    pr_key.write(private_key)

with open("public.pem", "wb") as pu_key:
    pu_key.write(public_key)
