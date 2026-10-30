# Custom TLS 1.3 Handshake Engine

An educational implementation of a TLS-style secure communication handshake using **ECDHE, HKDF-SHA256, and AES-256-GCM** in Python.

## Overview

This project demonstrates the core cryptographic concepts involved in establishing secure communication between a client and a server.

It simulates how two parties can independently generate a shared secret, derive a symmetric encryption key, and securely exchange an encrypted message.

## Objectives

- Understand the working principles of a TLS-style handshake.
- Implement Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange.
- Derive a symmetric key using HKDF with SHA-256.
- Encrypt and decrypt messages using AES-GCM.
- Verify that both parties derive the same shared secret and encryption key.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11+ | Core implementation |
| cryptography | Cryptographic operations |
| ECDHE | Shared secret generation |
| HKDF-SHA256 | Symmetric key derivation |
| AES-256-GCM | Authenticated encryption |

## Project Workflow

1. **Environment Setup:** Create a Python virtual environment and install the required library.
2. **Key Generation:** Generate separate elliptic curve key pairs for the client and server.
3. **ECDHE Key Exchange:** Exchange public keys and independently calculate the shared secret.
4. **Key Derivation:** Use HKDF-SHA256 to derive a 32-byte encryption key.
5. **Message Encryption:** Encrypt the message using AES-256-GCM.
6. **Message Decryption:** Decrypt the ciphertext using the derived key.
7. **Verification:** Check whether both parties generated matching secrets and successfully recovered the original message.

## Project Structure

```text
tls-handshake-engine/
│
├── src/
│   └── key_exchange.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/tls-handshake-engine.git
```

### 2. Navigate to the Project

```bash
cd tls-handshake-engine
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

Execute the following command:

```bash
python src/key_exchange.py
```

## Expected Results

The program demonstrates:

- Successful ECDHE shared-secret generation.
- Matching shared secrets on both client and server.
- Matching HKDF-derived encryption keys.
- Successful AES-GCM message encryption and decryption.
- Recovery of the original plaintext message.

Example output:

```text
Shared secrets match: True
Derived keys match: True
Key length: 32 bytes

Original message: Hello, server!
Decrypted message: Hello, server!
Message received correctly: True
```

*Note: Exact output formatting may differ depending on the implementation.*

## Learning Outcomes

Through this project, we understand:

- Public-key cryptography and key exchange.
- Elliptic Curve Cryptography (ECC).
- Key derivation using HKDF.
- Authenticated encryption using AES-GCM.
- The role of cryptographic keys in secure communication.

## Project Scope

This is an educational TLS-style handshake simulation designed to demonstrate selected cryptographic operations. It is not a complete or production-ready
