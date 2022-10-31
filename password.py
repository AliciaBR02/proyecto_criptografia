import hashlib
import os

class Password:
    def __init__(self, password):
        self.__password = password
        self.__hashed_password = self.hash_password(password)
        self.__salt = os.urandom(32)
        self.encrypted_salt = self.encrypt_salt()

    def hash_password(self, password):
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.__salt, 100000)

    def save_password(self):
        # with open('database/secure_passwords.json', 'a') as file:
        #     file.write(str(self.__salt) + '\n')
    
    def encrypt_salt(self):
        # encriptar con la clase de encriptación