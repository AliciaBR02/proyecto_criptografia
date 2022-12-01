"""This file will contain the functions of the user 'teacher'"""
import json_manager
from password_secure import PasswordSecure
from sign_verification import SignVerification
from encryption import Encryption
import os

class Teacher:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        p = PasswordSecure(password)
        self.password = p.hashed_password
        self.subjects = subjects
        s = SignVerification()
        private_key = s.generate_private_key()
        # encriptamos la key
        self.private_key = s.encrypt_private_key(private_key, password).decode('utf-8')
        public_key = s.generate_public_key(private_key)
        self.public_key = s.encrypt_public_key(public_key).decode('utf-8')


    
    def register(self):
        # save the data in the teacher database
        database = json_manager.JsonManager('database/teachers_database.json')
        database.add_item(self)
        
    def generate_private_key(self, password):
        s = SignVerification()
        key = s.generate_private_key()
        # save the key encrypted into a pem file
        encrypted_key = Encryption(self.email, password).encrypt(key)
        return encrypted_key

# t = Teacher('Juan', 'Perez', 'profesor@mail.com', '1234', ['Mathematics', 'Physics'])
# t.register()