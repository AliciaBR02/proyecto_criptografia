"""This file will contain the functions of the user 'teacher'"""
import json_manager
from password_secure import PasswordSecure
from sign_verification import SignVerification
from encryption import Encryption

class Teacher:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        p = PasswordSecure(password)
        self.password = p.hashed_password
        self.subjects = subjects
        s = SignVerification()
        key = s.generate_private_key()
        self.private_key = PasswordSecure(key).hashed_password
        # self.private_key = self.generate_private_key(password)


    
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

t = Teacher('Juan', 'Perez', 'profesor@mail.com', '1234', ['Mathematics', 'Physics'])
t.register()