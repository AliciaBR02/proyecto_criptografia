import hashlib
# from Crypto import Random
# from Crypto.Cipher import AES
# from base64 import b64encode, b64decode
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import hmac
from hashlib import md5
from json_manager import JsonManager

class Encryptation:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.encrypted = ""

    def encrypt(self, message, path):
        # print(path)
        key = self.key
        f = Fernet(key)
        self.encrypted = f.encrypt(message.encode('utf-8')).decode('utf-8')
        self.key = self.key.decode('utf-8')
        JsonManager(path).add_item(self)
        return self.encrypted
    
    def decrypt(self, encrypted, path):
        with open(path,'rb') as file:
            key = file.read()
        f = Fernet(key)
        print(encrypted)
        decrypted = f.decrypt(encrypted).decode('utf-8')
        return decrypted
    

# e = Encryptation()
# message = "Hello World!"
# encrypted = e.encrypt(message)
# print(e.decrypt(encrypted))
