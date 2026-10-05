# Cryptography Basics

## 1. Introduction

Cryptography is the practice of protecting information by transforming it into a form that unauthorized users cannot easily understand.

Cryptography is used to provide security properties such as:

- Confidentiality
- Integrity
- Authentication
- Non-repudiation

Cryptographic techniques are commonly used in secure communication, websites, authentication systems, digital certificates, and data protection.

---

## 2. Encryption

Encryption is the process of converting readable data, called plaintext, into an unreadable form called ciphertext using a cryptographic algorithm and a key.

```text
Plaintext
    |
    | Encryption + Key
    ↓
Ciphertext
```

Decryption reverses this process:

```text
Ciphertext
    |
    | Decryption + Key
    ↓
Plaintext
```

Encryption is mainly used to provide **confidentiality**.

---

# 3. Symmetric Encryption

Symmetric encryption uses the **same secret key** for both encryption and decryption.

```text
             Same Secret Key
                  |
                  ↓
Plaintext → Encryption → Ciphertext
                              |
                              ↓
                         Decryption
                              |
                              ↓
                           Plaintext
```

The sender and receiver must securely share the secret key.

### Advantages

- Fast
- Efficient for large amounts of data
- Suitable for file and disk encryption

### Disadvantages

- The secret key must be securely shared.
- If the key is compromised, the encrypted data may be compromised.

### Examples

Common symmetric encryption algorithms include:

- AES
- 3DES
- ChaCha20

AES is widely used for modern encryption.

---

# 4. Asymmetric Encryption

Asymmetric encryption uses a **pair of keys**:

- Public key
- Private key

The public key can be shared with others, while the private key should be kept secret.

```text
Public Key  → Used for encryption
Private Key → Used for decryption
```

For example:

```text
Plaintext
    |
    | Encrypt with Public Key
    ↓
Ciphertext
    |
    | Decrypt with Private Key
    ↓
Plaintext
```

### Advantages

- No need to share the private key.
- Useful for secure key exchange and authentication.
- Supports digital signatures.

### Disadvantages

- Generally slower than symmetric encryption.
- Requires more computational resources.

### Examples

Common asymmetric cryptographic algorithms include:

- RSA
- ECC
- Diffie-Hellman

---

# 5. Symmetric vs Asymmetric Encryption

| Feature | Symmetric | Asymmetric |
|---|---|---|
| Keys | One shared secret key | Public and private key pair |
| Speed | Faster | Generally slower |
| Key sharing | Secret key must be shared securely | Public key can be shared |
| Main uses | Bulk data encryption | Key exchange, authentication, digital signatures |
| Examples | AES, ChaCha20 | RSA, ECC |

In modern secure communication, both approaches are often used together. Asymmetric cryptography can help establish or protect a session key, while symmetric encryption can efficiently protect the actual data.

---

# 6. Hashing

Hashing is the process of converting input data into a fixed-length value called a hash or digest.

Unlike encryption, hashing is designed to be a **one-way process**.

```text
Input Data
    |
    | Hash Function
    ↓
Hash Value
```

A hash is commonly used to verify data integrity.

If the original data changes, the resulting hash should also change.

---

# 7. MD5

MD5 stands for Message-Digest Algorithm 5.

MD5 produces a **128-bit hash value**, commonly represented as a 32-character hexadecimal string.

Example:

```bash
echo -n "Hello" | md5sum
```

MD5 is considered cryptographically broken because attackers can create collisions in which different inputs produce the same hash.

Therefore, MD5 should **not** be used for security-sensitive applications such as password storage or digital signatures.

It may still be encountered when verifying the integrity of non-security-critical files.

---

# 8. SHA-256

SHA-256 is a member of the SHA-2 family of cryptographic hash functions.

It produces a **256-bit hash value**, normally represented as a 64-character hexadecimal string.

Example:

```bash
echo -n "Hello" | sha256sum
```

SHA-256 is significantly stronger than MD5 and is widely used for integrity verification and various security applications.

---

# 9. MD5 vs SHA-256

| Feature | MD5 | SHA-256 |
|---|---|---|
| Hash size | 128 bits | 256 bits |
| Hexadecimal representation | 32 characters | 64 characters |
| Collision resistance | Broken | Much stronger |
| Recommended for security | No | Yes, for appropriate uses |
| Common use | Legacy integrity checks | Integrity verification and security applications |

### Important

Hashing and encryption are different.

**Encryption:**
- Designed to be reversible with the appropriate key.
- Used mainly for confidentiality.

**Hashing:**
- Designed to be one-way.
- Used for integrity verification and other security applications.

---

# 10. Digital Certificates

A digital certificate is an electronic document used to associate a public key with an identity.

Digital certificates are commonly used with HTTPS and TLS.

A certificate can contain information such as:

- Subject/domain name
- Public key
- Certificate issuer
- Validity period
- Serial number
- Digital signature of the certificate authority

---

# 11. Certificate Authority

A Certificate Authority (CA) is a trusted organization that issues and signs digital certificates.

The CA verifies information according to its certificate issuance process and digitally signs the certificate.

A simplified trust model is:

```text
Certificate Authority
        |
        | Signs Certificate
        ↓
Digital Certificate
        |
        ↓
Website / Server
```

When a browser connects to an HTTPS website, it can validate the certificate and its trust chain.

---

# 12. SSL/TLS

TLS stands for Transport Layer Security.

TLS is a cryptographic protocol used to secure communication over networks.

SSL (Secure Sockets Layer) is the older technology that preceded TLS. Modern systems should use current TLS versions rather than obsolete SSL versions.

TLS can provide:

- Confidentiality
- Integrity
- Authentication

HTTPS uses HTTP over TLS.

```text
HTTP
  +
TLS
  ↓
HTTPS
```

The standard HTTPS port is:

```text
443
```

---

# 13. Simplified TLS Communication

A simplified view of secure HTTPS communication is:

```text
Client
   |
   | Connect to Server
   ↓
Server
   |
   | Sends Certificate
   ↓
Client validates certificate
   |
   | Secure TLS handshake
   ↓
Session established
   |
   | Encrypted communication
   ↓
Secure data exchange
```

The actual TLS handshake is more detailed and depends on the TLS version and cipher suites being used.

---

# 14. OpenSSL

OpenSSL is an open-source toolkit that implements cryptographic protocols and provides command-line tools for cryptographic operations.

It can be used for:

- Encryption and decryption
- Hash generation
- Key generation
- Certificate management
- TLS testing

OpenSSL is commonly available on Linux systems.

Check the installed version using:

```bash
openssl version
```

---

# 15. OpenSSL Encryption and Decryption

For the practical part of this task, a test message can be encrypted and then decrypted using OpenSSL.

The process is:

```text
Plaintext
    |
    | OpenSSL Encryption
    ↓
Encrypted File
    |
    | OpenSSL Decryption
    ↓
Original Plaintext
```

### Step 1: Create a test message

```bash
echo "This is a cybersecurity lab test message." > message.txt
```

View the message:

```bash
cat message.txt
```

### Step 2: Encrypt the message

A symmetric encryption method such as AES can be used.

```bash
openssl enc -aes-256-cbc -salt -pbkdf2 -in message.txt -out message.enc
```

OpenSSL will ask for a password.

The encrypted file can then be checked:

```bash
ls -l message.txt message.enc
```

### Step 3: Decrypt the message

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -in message.enc -out decrypted.txt
```

Enter the same password used during encryption.

### Step 4: Verify the decrypted message

```bash
cat decrypted.txt
```

The original message should be displayed.

### Expected Result

The encrypted file should not display the original readable message, while the decrypted file should contain the original text.

---

# 16. OpenSSL Hashing

OpenSSL can also generate cryptographic hashes.

For example:

```bash
echo -n "Hello" | openssl dgst -sha256
```

This calculates the SHA-256 digest of the input.

---

# 17. Practical Lab Exercise

The OpenSSL practical demonstrates the basic encryption and decryption process.

### Commands used

Create the message:

```bash
echo "This is a cybersecurity lab test message." > message.txt
```

Encrypt:

```bash
openssl enc -aes-256-cbc -salt -pbkdf2 -in message.txt -out message.enc
```

Decrypt:

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -in message.enc -out decrypted.txt
```

Verify:

```bash
cat decrypted.txt
```

The decrypted output should match the original message.

---

# 18. Security Considerations

Cryptographic security depends not only on the algorithm but also on how it is implemented and managed.

Important considerations include:

- Use modern and well-reviewed algorithms.
- Protect cryptographic keys and passwords.
- Avoid obsolete algorithms such as MD5 for security-sensitive purposes.
- Use modern TLS configurations.
- Keep cryptographic software updated.
- Use secure key management practices.
- Never expose private keys or encryption passwords unnecessarily.

---

# 19. Summary

| Concept | Purpose |
|---|---|
| Symmetric Encryption | Encrypts and decrypts using a shared secret key |
| Asymmetric Encryption | Uses public and private keys |
| Hashing | Produces a one-way digest of data |
| MD5 | Legacy hash algorithm with known security weaknesses |
| SHA-256 | Stronger hash function from the SHA-2 family |
| Digital Certificate | Associates an identity with a public key |
| Certificate Authority | Issues and signs trusted certificates |
| TLS | Provides secure communication over networks |
| HTTPS | HTTP protected using TLS |
| OpenSSL | Toolkit for cryptographic and TLS operations |

## Conclusion

Cryptography is an important part of cybersecurity because it helps protect data, verify integrity, and establish trust between systems. Symmetric and asymmetric encryption provide different approaches to protecting information, while hashing is primarily used for integrity and other one-way operations. Digital certificates and TLS help establish secure communication on networks.

The OpenSSL practical demonstrates how a plaintext message can be encrypted into ciphertext and then decrypted back into its original form using a password-based symmetric encryption process.
````
