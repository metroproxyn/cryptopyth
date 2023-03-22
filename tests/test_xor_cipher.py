import src.xor_cipher as xor_cipher

message = "Hello, world!"
key = "secret"

# Encrypt the message
encrypted_message = xor_cipher(message, key)

# Decrypt the message
decrypted_message = xor_cipher(encrypted_message, key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)