def caesar_encrypt(text, shift):
    result = ""
    # iterate through each character in the input text
    for char in text:
        # check if character is an uppercase or lowercase letter
        if char.isalpha():
            # shift the character by the specified number of positions
            char_code = ord(char) + shift
            # handle wraparound for positions beyond 'Z' or 'z'
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            
            # append the shifted character to the result string
            result += chr(char_code)       
        else:
            # append non-letter characters as-is
            result += char

    return result

# ToDo
# Write a decryptor, change caesar_cipher function name to the encryptor
def caesar_decrypt(text, shift):
    result = ""
    #ToDo: iterate through each character in the input text
    return result
