import rsa

# Load private key
with open('private_key.pem', 'rb') as f:
    private_key_data = f.read()
    private_key = rsa.PrivateKey.load_pkcs1(private_key_data)

# Load public key
with open('public_key.pem', 'rb') as f:
    public_key_data = f.read()
    public_key = rsa.PublicKey.load_pkcs1(public_key_data)

with open("message_file.txt", "rb") as f:  # Note the 'rb' mode to read in binary mode
    message = f.read()
    f.close()

# Hash the message
with open('message_file.txt', 'rb') as msgfile:
    signature = rsa.sign(msgfile, private_key, 'SHA-1')


with open('message_file_signature.txt', 'wb') as msgfile:
    msgfile.write(signature)
