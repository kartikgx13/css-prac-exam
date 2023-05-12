def encrypt(plaintext,n):
    ans=""

    for ch in plaintext:
        if ch==" ":
            ans += " "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65 )% 26 + 65)
        else:
            ans += chr((ord(ch) + n-97 )% 26 + 97)
    
    return ans

def decrypt(plaintext,n):
    ans=""

    for ch in plaintext:
        if ch==" ":
            ans += " "
        elif (ch.isupper()):
            ans += chr((ord(ch) - n-65 )% 26 + 65)
        else:
            ans += chr((ord(ch) - n-97 )% 26 + 97)
    
    return ans


#main driver code
message=input("Enter message")
key=int(input("Enter key"))
res_enc=encrypt(message,key)
res_dec=decrypt(res_enc,key)
print(f"Encrypted text: {res_enc}")
print(f"Decrypted text: {res_dec}")