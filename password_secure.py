import hashlib
import os
from json_manager import JsonManager
import binascii

class PasswordSecure:
    def __init__(self, password):
        # create a salt, then hash the password and get a key
        self.salt = os.urandom(32)
        self.hashed_password = binascii.hexlify(self.hash_password(password, self.salt)).decode()
        self.key = self.create_key(password)
        # save all the data
        self.save_password()
        
    def save_password(self):
        # save salt and hashed password in a json file
        self.salt = binascii.hexlify(self.salt).decode()
        self.key = binascii.hexlify(self.key).decode()
        JsonManager("database/secure_passwords.json").add_item(self)
    
    def create_key(self, password):
        # create a key from the password
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100000)

    @staticmethod
    def hash_password(password, salt):
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 200000)
