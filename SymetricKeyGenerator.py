import secrets

def generate_symmetric_key(key_length):
   # Generate a random key with the specified length
   key = secrets.token_bytes(key_length)
   return key

# Create a symmetric key with a length of 32 bytes (256 bits)
key = generate_symmetric_key(32)
print("Symmetric Key:", key.hex())
