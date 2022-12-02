import hashlib
import os
from json_manager import JsonManager
import binascii
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

class PasswordSecure:
    def __init__(self, password):
        # create a random salt
        salt = os.urandom(32)
        self.salt = salt
        # hash the password with the created salt
        self.hashed_password = binascii.hexlify(self.hash_password(password, self.salt)).decode()
        # create a key derivating from the salt and the password
        self.save_password()
        
    def save_password(self):
        """Save the password and the salt in a json file"""
        self.salt = binascii.hexlify(self.salt).decode()
        JsonManager("database/secure_passwords.json").add_item(self)
    
    @staticmethod
    def hash_password(password, salt):
        """Hash the password with the salt"""
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 200000)
