# Enter the approved prime number and the primitive root g.
Prime_no = int(input("Enter Prime No. p : "))
g = int(input("Enter Primitive root (g<p) : "))
# Enter chosen private key
PkXa = int(input("Enter Private key of A (xa<p) : "))
PkXb = int(input("Enter Private key of B (xb<p) : "))
# Calculate public key of both
ya = g**PkXa % Prime_no
yb = g**PkXb % Prime_no
# Calculate shared secret key K
ka = yb**PkXa % Prime_no
kb = ya**PkXb % Prime_no
print("A’s Public Key Ya =",ya)
print("B’s Public Key Yb =",yb)
print("Shared secret key k =",ka,kb)