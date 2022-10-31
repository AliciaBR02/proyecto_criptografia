import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os

class Encryptation:
    def __init__(self):
        self.key = os.urandom(16)
        self.block_size = AES.block_size
        # self.cipher = AES.new(self.key, AES.MODE_CBC, self.key)
        self._pad = lambda s: s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)
        self._unpad = lambda s: s[:-ord(s[len(s) - 1:])]


    # def encrypt(self, raw):
    #     raw = self._pad(raw)
    #     return b64encode(self.cipher.encrypt(raw))
    
    # def decrypt(self, enc):
    #     enc = b64decode(enc)
    #     return self.cipher.decrypt(enc).rstrip('\0')
    
    
    # def encrypt(plain_text, key):
    # private_key = hashlib.sha256(key.encode("utf-8")).digest()
    # plain_text = pad(plain_text)
    # print("After padding:", plain_text)
    # iv = Random.new().read(AES.block_size)
    # cipher = AES.new(private_key, AES.MODE_CBC, iv)
    # return base64.b64encode(iv + cipher.encrypt(plain_text))

    def encrypt(self, plain_text):
        plain_text = self._pad(plain_text)
        # iv = Random.new().read(self.block_size)
        # nonce = os.urandom(16)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")
    
    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self._unpad(plain_text)



#     def decrypt(cipher_text, key):
#         private_key = hashlib.sha256(key.encode("utf-8")).digest()
#         cipher_text = base64.b64decode(cipher_text)
#         iv = cipher_text[:16]
#         cipher = AES.new(private_key, AES.MODE_CBC, iv)
#         return unpad(cipher.decrypt(cipher_text[16:]))
    
message=input("Enter message to encrypt: ")
# key = input("Enter encryption key: ")
encrypted_msg = Encryptation().encrypt(message)
print("Encrypted Message:", encrypted_msg)
# decrypted_msg = decrypt(encrypted_msg, key)
# print("Decrypted Message:", bytes.decode(decrypted_msg))