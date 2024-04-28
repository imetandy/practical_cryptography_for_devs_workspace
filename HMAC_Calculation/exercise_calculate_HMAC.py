import hashlib, hmac, binascii

def hmac_sha384(key, msg): 
    return hmac.new(key, msg, hashlib.sha384).digest()

key = b'cryptography'
msg = b'hello'

print(binascii.hexlify(hmac_sha384(key, msg)))

key = b'again'
msg = b'hello'

print(binascii.hexlify(hmac_sha384(key, msg)))