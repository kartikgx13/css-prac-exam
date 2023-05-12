import random

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def generate_pair(p,q):
   
   n=p*q
   phi=(p-1)*(q-1)

   #calculating value of e such that e and phi are coprime

   e=random.randrange(1,phi)
   while gcd(e,phi)!=1:
       e=random.randrange(1,phi)
    
   #calculating mod inverse of d
   d= pow(e,-1,phi)

   return ((e,n),(d,n))

def encrypt(message,public_key):
    e,n=public_key
    cipher=[pow(ord(c),e,n) for c in message]
    return cipher

def decrypt(cipher,private_key):
    d,n=private_key
    messsage=[chr(pow(c,d,n)) for c in cipher]
    return "".join(messsage)

#main driver code
p=61
q=53
message="Kartik"
public_key,private_key=generate_pair(p,q)
print(f"Encrypted message: {encrypt(message,public_key)}")
print(f"Decrypted message: {decrypt((encrypt(message,public_key)),private_key)}")

