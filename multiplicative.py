def multiplicative_cipher_encrypt(message, key):
    """
    Encrypts a message using the multiplicative cipher.

    :param message: the message to encrypt
    :param key: the key to use for encryption (an integer between 1 and 25)
    :return: the encrypted message
    """
    # Convert the message to uppercase and remove spaces
    message = message.upper().replace(" ", "")

    # Encrypt the message by multiplying each character's ASCII code by the key
    cipher = ""
    for c in message:
        cipher += chr(((ord(c) - 65) * key) % 26 + 65)

    return cipher


def multiplicative_cipher_decrypt(cipher, key):
    """
    Decrypts a message using the multiplicative cipher.

    :param cipher: the cipher to decrypt
    :param key: the key to use for decryption (an integer between 1 and 25)
    :return: the decrypted message
    """
    # Decrypt the cipher by dividing each character's ASCII code by the key
    message = ""
    for c in cipher:
        message += chr(((ord(c) - 65) * pow(key, -1, 26)) % 26 + 65)

    return message


# Example usage:
message = "Hello, world!"
key = 7

cipher = multiplicative_cipher_encrypt(message, key)
print("Encrypted message:", cipher)

decrypted_message = multiplicative_cipher_decrypt(cipher, key)
print("Decrypted message:", decrypted_message)