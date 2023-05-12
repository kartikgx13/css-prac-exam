def encrypt_text(plaintext,n):
    ans = ""
# iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
# check if space is there then simply add space
        if ch==" ":
            ans+=" "
# check if a character is uppercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
# check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans

def decrypt_text(decrypttext,n):
    ans = ""
# iterate over the given text
    for i in range(len(decrypttext)):
        ch = decrypttext[i]
# check if space is there then simply add space
        if ch==" ":
            ans+=" "
# check if a character is uppercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) - n-65) % 26 + 65)
# check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) - n-97) % 26 + 97)
    return ans


plaintext = input("Enter the plain text: ")
n = int(input("Enter the Shift key: "))
res = encrypt_text(plaintext, n)
print('Cipher text: ', res)
res1 = decrypt_text(res, n)
print('Decrypted text: ', res1)