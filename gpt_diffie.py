import random

# Shared prime number
p = 23

# Shared base
g = 5

# Alice's private key
a_private = random.randint(1, p - 1)

# Bob's private key
b_private = random.randint(1, p - 1)

# Calculate Alice's public key
a_public = (g ** a_private) % p

# Calculate Bob's public key
b_public = (g ** b_private) % p

# Exchange public keys

# Alice calculates the shared secret key
a_shared_secret = (b_public ** a_private) % p

# Bob calculates the shared secret key
b_shared_secret = (a_public ** b_private) % p

# Both Alice and Bob now have the same shared secret key
print("Alice's shared secret key:", a_shared_secret)
print("Bob's shared secret key:", b_shared_secret)
