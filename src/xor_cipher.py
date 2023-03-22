def xor_cipher(message, key):

    ## TODO:
    # Convert the message and key to bytes
    message_bytes = message.encode()
    key_bytes = key.encode()

    # Calculate the lenght of the key
    key_length = len(key_bytes)

    # Create a bytearray to hold the encrypted_decrupted message
    # (The bytearray() method returns an array of bytes of the given size and initialization values.)
    result = bytearray(len(message_bytes))

    # Loop through the message and XOR each byte with the corresponding bytes in the key
    for i in range(len(message_bytes)):
        result[i] = message_bytes[i] ^ key_bytes[i % key_length]

    # Convert the bytearray to a string and return it
    return result.decode()