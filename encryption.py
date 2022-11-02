from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from json_manager import JsonManager
import base64

class Encryption:
    def __init__(self, email, password):
        self.key = self.get_key(email, password)
        self.encrypted = ""

    def encrypt(self, message):
        """Function to encrypt a message"""
        key = self.key
        if key == "key no found":
            return "key not found"
        # we create the fernet object, key will always enter as bytes
        f = Fernet(key)
        # we encrypt the message
        self.encrypted = f.encrypt(message.encode('utf-8')).decode('utf-8')
        # we save the encrypted message in the database
        return self.encrypted
    
    def decrypt(self, encrypted):
        """Function to decrypt a message"""
        # database = JsonManager(path).data
        key = self.key
        # we create the fernet object, we will use the same key as the one used to encrypt
        f = Fernet(key)
        # we decrypt the message
        decrypted = f.decrypt(encrypted.encode('utf-8'))
        return decrypted.decode('utf-8')
    
    def get_key(self, email, password):
        """Function to get the key from the database"""
        database = JsonManager('database/students_database.json')
        password_database = JsonManager('database/secure_passwords.json').data
        for student in database.data:
            # we look for the email in the database
            if student['email'] == email:
                password_real = student['password']
                for key in password_database:
                    # check if the password is correct
                    if key['hashed_password'] == password_real:
                        # we get the salt and the key
                        kdf = PBKDF2HMAC(
                            algorithm=hashes.SHA256(),
                            length=32,
                            salt=key['salt'].encode('utf-8'),
                            iterations=100000,
                        )
                        key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))                        
                        return key
        return "key not found"
