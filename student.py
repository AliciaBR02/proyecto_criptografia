"""This file will contain the functions of the user 'Student'"""
import json_manager
from password_secure import PasswordSecure
from cryptography.hazmat.primitives.asymmetric import rsa

class Student:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        p = PasswordSecure(password)
        self.password = p.hashed_password
        self.subjects = subjects
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        # self.private_key = PasswordSecure(private_key).hashed_password
    
    def register(self):
        # save the data in the student database
        database = json_manager.JsonManager('database/students_database.json')
        database.add_item(self)


s = Student('Juan', 'Perez', 'estudiante@mail.com', '1234', ['Mathematics', 'Physics'])
s.register()