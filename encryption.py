import hashlib
# from Crypto import Random
# from Crypto.Cipher import AES
# from base64 import b64encode, b64decode
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import hmac
from hashlib import md5, scrypt
import json
from json_manager import JsonManager
import binascii
from login import Login
import base64

class Encryption:
    def __init__(self, email): #key = alg derivación (salt, contraseña)
        
        self.key = self.get_key(email)
        self.encrypted = ""

    def encrypt(self, message, path):
        # print(path)
        # key base 64
        key = self.key

        f = Fernet(key)
        self.encrypted = f.encrypt(message.encode('utf-8')).decode('utf-8')
        self.key = key.decode('utf-8')
        JsonManager(path).add_item(self)
        return self.encrypted
    
    def decrypt(self, encrypted, path):
        database = JsonManager(path).data
        key = ''
        for dic in database:
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
    
    def get_key(self, email):
        database = JsonManager('database/students_database.json')
        password_database = JsonManager('database/secure_passwords.json').data
        for student in database.data:
            # print(student['email'])
            if student['email'] == email:
                # comprobar que la password sea correcta
                password_real = student['password']
                for key in password_database:
                    if key['hashed_password'] == password_real:
                        backend = default_backend()
                        kdf = PBKDF2HMAC(
                            algorithm=hashes.SHA256(),
                            length=32,
                            salt=key['salt'].encode('utf-8'),
                            iterations=100000,
                            backend=backend
                        )
                        key = base64.urlsafe_b64encode(kdf.derive(key["key"].encode('utf-8')))
                        # return 32 url-safe base64-ecnoded bytes- key
                        # print(key)
                        return key
        raise Exception("key not found")
# e = encryption()
# message = "Hello World!"
# encrypted = e.encrypt(message)
# print(e.decrypt(encrypted))
