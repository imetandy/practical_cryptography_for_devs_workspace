from Crypto.Hash import keccak
import hashlib, binascii

text = 'hello'
data = text.encode('utf-8')

sha256hash = hashlib.sha256(data).digest()
print("SHA-256:     ",binascii.hexlify(sha256hash))

sha3_256 = hashlib.sha3_256(data).digest()
print("SHA3-256:     ",binascii.hexlify(sha3_256))

blake2s = hashlib.new('blake2s', data).digest()
print("BLAKE2S:     ",binascii.hexlify(blake2s))

ripmd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:     ",binascii.hexlify(ripmd160))

keccak256 = keccak.new(data=b'hello', digest_bits=256).digest()
print("KECCAK-256:     ",binascii.hexlify(keccak256))