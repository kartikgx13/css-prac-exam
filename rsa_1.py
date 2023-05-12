import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that e and phi are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    
    # Compute the modular inverse of e
    d = pow(e, -1, phi)
    
    return (e, n), (d, n)

def encrypt(public_key, message):
    e, n = public_key
    encrypted_msg = [pow(ord(c), e, n) for c in message]
    return encrypted_msg

def decrypt(private_key, encrypted_msg):
    d, n = private_key
    decrypted_msg = [chr(pow(c, d, n)) for c in encrypted_msg]
    return ''.join(decrypted_msg)

# Example usage:
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

message = "kartik"
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)
joined_numbers = ''.join(str(num) for num in encrypted_message)
print(joined_numbers)
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
