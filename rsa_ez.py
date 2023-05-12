import random

def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % m

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd_extended(e, phi)[0] != 1:
        e = random.randrange(1, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return ' '.join([str(char) for char in cipher])

def decrypt(private_key, ciphertext):
    d, n = private_key
    cipher = [int(char) for char in ciphertext.split()]
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)

# Example usage:
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)
message = "kartik"
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)