def encrypt(plaintext,key):
    #adding white space if necessary:
    #and this function will only be here as in decryption we will be stripping the white
    #spaces

    cipher=""
    if (len(plaintext)%key!=0):
        plaintext += " "*(key-len(plaintext)%key) #adding padding if length is odd
        #its ok even if dont write this just give even length input
    
    for i in range(key):
        for j in range(len(plaintext)//key):
            cipher += plaintext[j * key + i]
    
    return cipher

def decrypt(ciphertext,key):

    plaintext=""
    for i in range(len(ciphertext)//key):
        for j in range(key):
            plaintext += ciphertext[i + j*(len(ciphertext)//key)]
    
    return plaintext.strip()

#main driver code
pt=input("Enter plain text: ")
key=int(input("Enter displacement"))

res_enc=encrypt(pt,key)
res_dec=decrypt(res_enc,key)

print(f"Encrypted text is : {res_enc}")
print(f"Decrypted text is : {res_dec}")
    
