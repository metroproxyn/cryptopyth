import src.caesar_cipher as caesar_cipher

plaintext = "This is my first cipher."
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print(ciphertext)