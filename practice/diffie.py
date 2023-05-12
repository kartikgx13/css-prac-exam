#taking prime number and g from user
prime_no=int(input("Enter the prime no. "))
g=int(input("Enter the value of g: "))

#taking the value of private key of A and B from the user
Xa=int(input("Enter private key of A"))
Xb=int(input("Enter private key of B"))

#calculating the public for A and B
Ya=g**Xa%prime_no
Yb=g**Xb%prime_no

#calculating the shared secret key for A and B
ka=Yb**Xa%prime_no
kb=Ya**Xb%prime_no

print(f"Public key for A : {Ya}")
print(f"Public key for B : {Yb}")
print(f"Shared secret key ka : {ka} = kb : {kb}")