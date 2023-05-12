def encrypt(message,key):
    #converting the message to uppercase and removing whitespaces
    cipher=""
    message=message.upper().replace(" ","")

    for ch in message:
        cipher += chr(((ord(ch)-65)*key) % 26 + 65)
    
    return cipher

def decrypt(message,key):
    og_text=""
    for ch in message:
        og_text += chr(((ord(ch) - 65) * pow(key, -1, 26)) % 26 + 65)
    
    return og_text

#main driver code
plaintext=input("Enter message to encrypt: ")
key=int(input("Enter key to be used: "))
res_enc=encrypt(plaintext,key)
res_dec=decrypt(res_enc,key)
print(res_enc)
print(res_dec)