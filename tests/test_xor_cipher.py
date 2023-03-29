from src.xor_cipher import xor_cipher

message = "Hello, world!" # plaintext – what name is preferable?
key = "secret"

# Encrypt the message
encrypted_message = xor_cipher(message, key)

# Decrypt the message
decrypted_message = xor_cipher(encrypted_message, key)

print("Original message is", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)