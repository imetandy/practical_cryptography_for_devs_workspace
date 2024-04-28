import scrypt 

salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
passwd = b'p@$Sw0rD~7'
key = scrypt.hash(passwd, salt, N=16384, r=1024, p=1, buflen=64)
print("Derived key: ", key.hex())