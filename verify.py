import rsa

# Load public key
with open('public_key.pem', 'rb') as f:
    public_key_data = f.read()
    public_key = rsa.PublicKey.load_pkcs1(public_key_data)

with open("message_file.txt", "rb") as f:
    message = f.read()

with open('message_file_signature.txt', 'rb') as f:
    signature = f.read()

# Verify the signature
try:
    rsa.verify(message, signature, public_key)
    print("Signature is valid.")
except rsa.VerificationError:
    print("Signature is not valid.")
