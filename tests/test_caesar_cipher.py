import src.caesar_cipher as caesar_encrypt

plaintext = "This is my first cipher."
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
print(ciphertext)