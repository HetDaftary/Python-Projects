import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

bs, HASH_COUNT = AES.block_size, 1000
# Change the count when needed.
# Hash count gives the number of times, hash fucntion is applied.

def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encrypt(raw, key):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode()

def decrypt(enc, key):
    enc = enc.encode()
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def hash(key): # For authentication purpose
    ans = key
    for i in range(HASH_COUNT):
        ans = hashlib.sha512(ans.encode()).hexdigest()
    return ans

def hashEnc(key):
    ans = key
    for i in range(HASH_COUNT):
        ans = hashlib.sha256(ans.encode()).hexdigest()
    return ans