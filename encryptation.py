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
import json
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
        self.key = key.decode('utf-8')
        JsonManager(path).add_item(self)
        return self.encrypted
    
    def decrypt(self, encrypted, path):
        # print(encrypted)
        #look inside the file for the key
        with open(path,'rb') as file:
            data = file.read()
        data = data.decode('utf-8')
        # convert the string to a dictionary
        res = json.loads(data)
        key = ''
        # dec_encrypted = encrypted.decode('utf-8')
        # print(dec_encrypted)
        for dic in res:
            # print(dic["encrypted"])
            if dic["encrypted"] == encrypted:
                key = dic["key"]
                # print(key)
                # print("y")
                
        if key == "":
            return "key not found"
        f = Fernet(key)
        # print(encrypted)
        decrypted = f.decrypt(encrypted.encode('utf-8'))
        return decrypted.decode('utf-8')
    

# e = Encryptation()
# message = "Hello World!"
# encrypted = e.encrypt(message)
# print(e.decrypt(encrypted))
