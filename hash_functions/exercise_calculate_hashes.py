# In this exercise session, you are assigned to write some code to calculate cryptographic hashes. Write a program to calculate hashes of given text message: SHA-224, SHA-256, SHA3-224, SHA3-384, Keccak-384 and Whirlpool. Write your code in programming language of choice.

from Crypto.Hash import keccak, SHA3_224, SHA3_384, SHA256
import hashlib, binascii

text = 'hello'
data = text.encode('utf-8')

sha224hash = hashlib.sha224(data).digest()
print("SHA-224:     ",binascii.hexlify(sha224hash))
      
sha256hash = hashlib.sha256(data).digest()
print("SHA-256:     ",binascii.hexlify(sha256hash))

sha3_224 = hashlib.sha3_224(data).digest()
print("SHA3-224:     ",binascii.hexlify(sha3_224))
      
sha3_384 = hashlib.sha3_384(data).digest()
print("SHA3-384:     ",binascii.hexlify(sha3_384))
      
keccak384 = keccak.new(data=b'hello', digest_bits=384).digest()
print("KECCAK-384:     ",binascii.hexlify(keccak384))
      
# whirlpool = hashlib.new('whirlpool', data).digest()
# print("WHIRLPOOL:     ",binascii.hexlify(whirlpool))

## Following error: 
# hon3.11 -c whirlpool/pywhirlpool.c -o build/temp.macosx-13-arm64-cpython-311/whirlpool/pywhirlpool.o
#      whirlpool/pywhirlpool.c:411:29: error: expression is not assignable
#          Py_TYPE(&Whirlpooltype) = &PyType_Type;
#          ~~~~~~~~~~~~~~~~~~~~~~~ ^
#      1 error generated.
#      error: command '/usr/bin/clang' failed with exit code 1
#      [end of output]
#  
#  note: This error originates from a subprocess, and is likely not a problem # with pip.
#   ERROR: Failed building wheel for whirlpool