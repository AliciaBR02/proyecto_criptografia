from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from hashlib import md5, scrypt
from json_manager import JsonManager
import base64

class Encryption:
    def __init__(self, email):
        self.key = self.get_key(email)
        self.encrypted = ""

    def encrypt(self, message, path):
        key = self.key
        if key == "key no found":
            return "key not found"
        f = Fernet(key)
        self.encrypted = f.encrypt(message.encode('utf-8')).decode('utf-8')
        self.key = key.decode('utf-8')
        JsonManager(path).add_item(self)
        return self.encrypted
    
    def decrypt(self, encrypted, path):
        database = JsonManager(path).data
        key = ''
        for dic in database:
            if dic["encrypted"] == encrypted:
                key = dic["key"]
        if key == "":
            return "key not found"
        f = Fernet(key)
        decrypted = f.decrypt(encrypted.encode('utf-8'))
        return decrypted.decode('utf-8')
    
    def get_key(self, email):
        database = JsonManager('database/students_database.json')
        password_database = JsonManager('database/secure_passwords.json').data
        for student in database.data:
            # we look for the email in the database
            if student['email'] == email:
                # check if the password is correct
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
                        return key
        return "key not found"
