
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


# STEP 1: Generate the client's key pair
client_private_key = ec.generate_private_key(ec.SECP256R1())
client_public_key = client_private_key.public_key()

# STEP 2: Generate the server's key pair
server_private_key = ec.generate_private_key(ec.SECP256R1())
server_public_key = server_private_key.public_key()


# STEP 3: Client calculates the shared secret
client_shared_secret = client_private_key.exchange(
    ec.ECDH(),
    server_public_key
)

# STEP 4: Server calculates the shared secret
server_shared_secret = server_private_key.exchange(
    ec.ECDH(),
    client_public_key
)

print(
    "Client and server secrets match:",
    client_shared_secret == server_shared_secret
)


# STEP 5: Client derives key material using HKDF
client_hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=b"tls-learning-salt",
    info=b"handshake key",
)

client_key = client_hkdf.derive(client_shared_secret)


# STEP 6: Server independently derives key material
server_hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=b"tls-learning-salt",
    info=b"handshake key",
)

server_key = server_hkdf.derive(server_shared_secret)

print(
    "Client and server derived keys match:",
    client_key == server_key
)
print("Derived key length:", len(client_key))


# STEP 7: Client encrypts a message using AES-GCM
message = b"Hello, server!"

# Generate a fresh, random 12-byte nonce
nonce = os.urandom(12)

# Create an AES-GCM cipher using the client's derived key
client_aesgcm = AESGCM(client_key)

# Encrypt the message; output includes ciphertext and authentication tag
ciphertext = client_aesgcm.encrypt(
    nonce,
    message,
    None
)

print("Original message:", message.decode())
print("Encrypted message (hex):", ciphertext.hex())


# STEP 8: Server decrypts and verifies the message
server_aesgcm = AESGCM(server_key)

decrypted_message = server_aesgcm.decrypt(
    nonce,
    ciphertext,
    None
)

print("Decrypted message:", decrypted_message.decode())
print("Message received correctly:", decrypted_message == message)
